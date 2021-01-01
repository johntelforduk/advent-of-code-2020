# Advent of Code 2020
Solutions to [Advent of Code 2020](https://adventofcode.com/2020) puzzles.
### Installation
```
pip install pytest
pip install matplotlib
pip install pygame
pip install imageio
```
For details, see `requirements.txt`.
### Day 17 - Conway Cubes
Here is a visualisation of part 1.

![alt text](https://github.com/johntelforduk/advent-of-code-2020/blob/main/17-conway-cubes/visualisation.jpg "Conway Cubes visualisation.")

### Day 19 - Monster Messages, part 2
New formula for rule 8 is, 
```
8: 42 | 42 8
```
... which can be expanded as (for example),
```
42
42 42
42 42 42
42 42 42 ...
```
In other words,
```
8: (42)+
```
New formula for rule 11 is,
```
11: 42 31 | 42 11 31
```
... which can be expanded as (for example),
```
42 31
42 42 31 31
42 42 42 31 31 31...
```
This cannot be represented using regular expressions. Therefore, I've manually expanded out the sequences for these two rules (up to 7 times) in the file `input2.txt`.
### Day 20 - Jurassic Jigsaw
Here is a visualisation of part 2.

![alt text](https://github.com/johntelforduk/advent-of-code-2020/blob/main/20-jurassic-jigsaw/screenshot.jpg "Jurassic Jigsaw visualisation.")

### Day 24 - Lobby Layout
Here is a visualisation of the solution to part 1.

![alt text](https://github.com/johntelforduk/advent-of-code-2020/blob/main/24-lobby-layout/assets/day_0.jpg "Lobby Layout part 1.")

And here is an animation of the first 10 days of part 2.

![alt text](https://github.com/johntelforduk/advent-of-code-2020/blob/main/24-lobby-layout/assets/first_10_iterations.gif "Lobby Layout part 2.")
