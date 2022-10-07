

print("please enter your percentage grade: ")
ans = input()
grade = int(ans)
#print(ans)
#print(type(ans))

# Letter Grade

# Percentage	GPA


# F	0–59%	0.0
if grade >= 0 and grade <= 59:
	letter_grade = "F"
# D	60–69%	1.0
elif grade >= 60 and grade <= 69:
	letter_grade = "D"
# C	70–79%	2.0
elif grade >= 70 and grade <= 79:
	letter_grade = "C"
# B	80–89%	3.0
elif grade >= 80 and grade <= 89:
	letter_grade = "B"
# A	90–100%	4.0
elif grade >= 90 and grade <= 100:
	letter_grade = "A"
else:
	letter_grade = "Unknown percentage"

print(f"Your percentage grade is {grade} and American letter grade is {letter_grade}")
