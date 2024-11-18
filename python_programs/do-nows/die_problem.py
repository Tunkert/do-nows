import random, formatting_strings


def create_probem(num, other_num):
    return f"Each side of a fair {num}-sided die is labeled with a number 1 through {num} with a different number appearing on each face. If the die is rolled one-time, what is the probability of rolling a {roll}?"


def create_num(lower, upper):
    return random.randint(lower, upper)


f = open('./python_programs/do-nows/html_output/die-problem.html', 'w')

f.write(formatting_strings.head_string)

for i in range(16):
    f.write("\n\t\t\t<div class='row'>\n\t\t\t\t")
    die_sides = create_num(10, 18)
    roll = create_num(1, die_sides)
    f.write(f"\n\t\t\t\t<p>{create_probem(die_sides, roll)}</p>\n")
    f.write("\n\t\t\t</div>\n")
    if i != 0 and (i + 1) % 4 == 0:
        f.write("\n\t\t<div class='pb'></div>\n")


f.write(formatting_strings.close_string)
f.close()