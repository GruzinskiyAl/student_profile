
def mark_generation(full_mark):
    if full_mark in range(60, 67):
        simple_mark = 3
        eu_mark = 'E'
    elif full_mark in range(67, 75):
        simple_mark = 3
        eu_mark = 'D'
    elif full_mark in range(75, 82):
        simple_mark = 4
        eu_mark = 'C'
    elif full_mark in range(82, 90):
        simple_mark = 4
        eu_mark = 'B'
    elif full_mark in range(90, 101):
        simple_mark = 5
        eu_mark = 'A'
    else:
        simple_mark = 2
        eu_mark = 'F'
    return full_mark, simple_mark, eu_mark
