# Solution to day 21 of AOC 2020, Allergen Assessment.
# https://adventofcode.com/2020/day/21

import sys

VERBOSE = ('-v' in sys.argv)


def allergens_from_text(text: str) -> dict:
    """For parm string containing a list of foods, return a dictionary. Each item in dictionary is an allergen and
       the set of ingredients that might contain that allergens.

       Returned dictionary has items as follows,
       k = Name of the allergen.
       v = A list. Each item in the list is a set. Each set is the ingredients in each food that might contain
           the allergen."""

    possible = {}

    for food in text.split('\n'):                           # Foods start on separate lines.
        food_no_brackets = food.replace('(', '').replace(')', '')
        ingredients, allergens = food_no_brackets.split(' contains ')

        ingredient_set = set()                              # The set of ingredients that might include this allergen.
        for ingredient in ingredients.split(' '):           # Ingredients are delimited with spaces.
            ingredient_set.add(ingredient)

        for allergen in allergens.split(', '):              # Allergens are delimited with comma + space.

            if allergen not in possible:
                possible[allergen] = [ingredient_set]
            else:
                possible[allergen].append(ingredient_set)

    return possible


def intersect_list(list_of_sets: list) -> str:
    """Parm is a list of sets. Each item in each set is a string, for example,
       [{'a', 'b, 'c', 'd'}, {'b'}]

       If the intersection of the list of sets is a single item, then that item is returned,
       otherwise 'None' is returned.

       So in the example above, 'b' is returned."""

    intersection_so_far = set()
    first = True
    for each_set in list_of_sets:
        if first:
            intersection_so_far = each_set
            first = False                       # No longer the first set in the list.
        else:
            intersection_so_far = intersection_so_far.intersection(each_set)

    if len(intersection_so_far) == 1:
        for i in intersection_so_far:
            return i

    return 'None'


def reduce_ingredients(allergens: dict) -> (dict, set):
    """For a parm dictionary of allergens (k = Allergens, v = list of sets, where each set is the list of
       ingredients in each feed that might contain the allergen).
       Reduce the number of ingredients that might contain an allergen, by looking for ingredients that are in all
       of the foods in the list for each allergen.
       Returns a reduced dictionary, plus a set of allergens that are now matched to a single ingredient."""
    solved = {}
    solved_ingredients = set()

    for allergen in allergens:
        ingredient_sets = allergens[allergen]

        intersection = intersect_list(ingredient_sets)

        if VERBOSE:
            print('allergen, ingredient_sets, intersection:', allergen, ingredient_sets, intersection)

        # This allergen must be in 1 specific ingredient.
        # So, make a note of that.
        if intersection != 'None':
            solved[allergen] = intersection
            solved_ingredients.add(intersection)

    if VERBOSE:
        print('solved, solved_ingredients:', solved, solved_ingredients)

    # For allergens that we've just solved (we know which ingredient they are in). Remove that ingredient from
    # Sets of potential ingredients for other allergens.
    result = {}
    for allergen in allergens:

        if allergen in solved:
            ingredient = solved[allergen]
            result[allergen] = [{ingredient}]
        else:
            ingredient_list = allergens[allergen]

            if VERBOSE:
                print('ingredient_list:', ingredient_list)
            new_list = []

            for ingredient_set in ingredient_list:
                new_set = set()
                for ingredient in ingredient_set:
                    if ingredient not in solved_ingredients:
                        new_set.add(ingredient)
                new_list.append(new_set)
            result[allergen] = new_list

    return result, solved_ingredients


def count_non_allergen_ingredients(text: str, allergen_ingredients: set) -> int:
    """For parm text which is puzzle input, and parm set of ingredients which are known to be allergens. Return a
       count of the number of non-allergen ingredients listed in recipes."""
    count = 0

    for food in text.split('\n'):
        ingredients, _ = food.split(' (')
        for ingredient in ingredients.split(' '):
            if ingredient not in allergen_ingredients:
                count += 1
    return count


def main():
    filename = sys.argv[1]

    f = open(filename)
    whole_text = f.read()
    f.close()

    allergens = allergens_from_text(whole_text)

    if VERBOSE:
        print('allergens:', allergens)

    done = False
    previous_length = 0
    allergen_ingredients = set()
    while not done:                     # Keep repeating until reduce_ingredients is not reducing anymore.
        allergens, allergen_ingredients = reduce_ingredients(allergens)

        if VERBOSE:
            print('allergens, solved:', allergens, allergen_ingredients)

        done = (previous_length == len(allergen_ingredients))
        previous_length = len(allergen_ingredients)

    print('Part 1:', count_non_allergen_ingredients(whole_text, allergen_ingredients))


if __name__ == "__main__":
    main()
