require_relative 'formatting_strings'

def create_parallelogram_problem
    a = rand(1..10)
    b = rand(1..10)
    total = 2 * a + 2 * b
    "\n<p> The equation #{total} = 2a + 2b gives you the relationship between the side lengths <var>a</var> and <var>b</var> of a certain parallelogram. If <var>a</var> = #{a}, what is the value of <var>b</var>?</p>\n"
end

f = File.open('./ruby_programs/html_outputs/parallelogram.html', 'w')
f.write($head_string)

i = 0
while i < 16 do
    f.write("<div class='row'>\n")
    f.write(create_parallelogram_problem())
    f.write("</div>\n")
    i += 1
end

f.write($close_string)
f.close