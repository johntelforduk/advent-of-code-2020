# Prints visualisation of the sequences.

for t in range(500):

    if t % 5 == 0:
        a = 'D'
    else:
        a = '-'
    if t % 7 == 0:
        b = 'D'
    else:
        b = '-'
    if t % 13 == 0:
        c = 'D'
    else:
        c = '-'

    print(t, a, b, c)
