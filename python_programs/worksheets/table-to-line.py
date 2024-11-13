import random

style_string = "\n<style>\n.container { margin: 0 0.5in; }\n.row { display: flex; justify-content: space-between;}\n.problem {width: 45%;}\n.pb {page-break-before: always;}</style>\n"
head_string = f"<!doctype html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>Table to Line</title>\n{style_string}\n</head>\n<body>\n<div class='container'>\n"
close_string = "\n</div>\n</body>\n</html>"


def create_table(idx):
    beginning_of_str = f'<h2>Problem {idx}</h2>\n<table border="1" cellspacing="0" cellpadding="15">\n\t<tr>\n\t\t<th>\n\t\t\tx\n\t\t</th>\n\t\t<th>\n\t\t\ty\n\t\t</th>\n\t\t</tr>\n'
    size_of_table = random.randint(4, 6)
    slope = random.randint(3, 10)
    slope_sign = random.randint(1, 2)
    if slope_sign == 1:
        slope *= -1
    initial_x_val = random.randint(-5, 5)
    initial_y_val = random.randint(-5, 5)
    base_str = ''
    for j in range(size_of_table):
        base_str += f'\t<tr>\n\t\t<td>\n\t\t\t{initial_x_val + initial_x_val * j * slope}\n\t\t</td>\n\t\t<td>\n\t\t\t{initial_y_val + j}\n\t\t</td>\n\t</tr>\n'
    end_of_str = '</table>\n'
    return f'<div class="problem">\n{beginning_of_str}{base_str}{end_of_str}\n</div>\n'


f = open('./html_outputs/table-to-line.html', 'w')
f.write(head_string)
f.write('<p>Translate the following x,y table into a line, then write down the three forms of the line (standard, slope-intercept, & point-slope)</p>\n')

for i in range(10):
    if i % 2 == 0:
        f.write('\n<div class="row">\n')
    f.write(create_table(i + 1))
    if i % 2 != 0:
        f.write('\n</div>\n')
    if i % 4 == 0 and i != 0:
        f.write('<div class="pb"></div>')


f.write(close_string)
f.close()
