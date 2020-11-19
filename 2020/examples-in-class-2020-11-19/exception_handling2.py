
result1 = 10 / 5
print(f"result: {result1}")

try:
	result2 = 10 / 0
	# Since we do not hand above error, below lines will not execute.
	print(f"result: {result2}")
except:
	print("error occurred")

result3 = 10 / 2
print(f"result: {result3}")
