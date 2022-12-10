print("please enter a number N")
s_number = input()
N = int(s_number)

print(N)

total = sum(range(0,N+1,3))

print(f"total of numbers up to {N} which are divisible by 3 is {total}")