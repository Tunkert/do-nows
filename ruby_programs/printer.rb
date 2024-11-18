require_relative 'formatting_strings'

def create_printer_problem
  printing_per_minute = rand(40..80)
  "\<p>A printer produces posters at a constant rate of #{printing_per_minute} posters per minute. At what rate, in posters per <u>hour</u>, does the printer produce the posters?</p>\n"
end

f = File.open('./ruby_programs/html_outputs/printers.html', 'w')
f.write($head_string)

i = 0
while i < 16 do
    f.write("<div class='row'>\n")
    f.write(create_printer_problem)
    f.write("</div>\n")
    i += 1
end

f.write($close_string)
