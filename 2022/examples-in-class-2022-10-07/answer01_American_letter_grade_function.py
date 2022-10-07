def find_american_letter_grade(grade):
	if grade >= 0 and grade <= 59:
		letter = "F"
	# D	60–69%	1.0
	elif grade >= 60 and grade <= 69:
		letter = "D"
	# C	70–79%	2.0
	elif grade >= 70 and grade <= 79:
		letter = "C"
	# B	80–89%	3.0
	elif grade >= 80 and grade <= 89:
		letter = "B"
	# A	90–100%	4.0
	elif grade >= 90 and grade <= 100:
		letter = "A"
	else:
		letter = "Unknown percentage"

	return letter

print("please enter your percentage grade: ")
ans = input()
grade = int(ans)

letter_grade = find_american_letter_grade(grade)

print(f"Your percentage grade is {grade} and American letter grade is {letter_grade}")
