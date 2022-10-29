
"""
  *
 ***
*****
"""

line_count = 10
maximum_number_of_stars = line_count * 2 - 1
for index in range(1,line_count+1):
	how_many_stars = index * 2 - 1
	line = "*" * how_many_stars
	line = line.center(maximum_number_of_stars)
	print(line)
