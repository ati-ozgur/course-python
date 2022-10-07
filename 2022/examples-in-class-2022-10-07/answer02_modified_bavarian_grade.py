def calculate_modified_bavarian_grade(maximum_possible_grade,minimum_possible_grade,actual_grade)
	modified_bavarian_grade = ((maximum_possible_grade - actual_grade) / (maximum_possible_grade -minimum_possible_grade )) * 3 + 1
	return modified_bavarian_grade


print("please enter your minimum possible grade: ")
answer = input()
minimum_possible_grade = int(answer)
print("please enter your maximum possible grade: ")
answer = input()
maximum_possible_grade = int(answer)
print("please enter your actual grade: ")
answer = input()
actual_grade = int(answer)

print(f"your minimum_possible_grade: {minimum_possible_grade}")
print(f"your maximum_possible_grade: {maximum_possible_grade}")
print(f"your actual_grade: {actual_grade}")

modified_bavarian_grade = calculate_modified_bavarian_grade(maximum_possible_grade,minimum_possible_grade,actual_grade)

print(f"Your Modified Bavarian: {modified_bavarian_grade}")
