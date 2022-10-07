print("please enter your minimum possible grade: ")
answer = input()
a = int(answer)
print("please enter your maximum possible grade: ")
answer = input()
b = int(answer)
print("please enter your actual grade: ")
answer = input()
c = int(answer)

print(f"your minimum_possible_grade: {a}")
print(f"your maximum_possible_grade: {b}")
print(f"your actual_grade: {c}")

d = ((b - c) / (b -a )) * 3 + 1

print(f"Your Modified Bavarian: {d}")
