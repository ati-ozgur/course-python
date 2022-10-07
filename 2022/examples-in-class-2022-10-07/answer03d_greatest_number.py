print("please enter numbers with spaces between them: ")
answer = input()
numbers_str = answer.split(" ")
numbers = [float(num) for num in numbers_str ]


greatest = max(numbers)


print(f"numbers are {numbers_str} and greatest is {greatest}")

