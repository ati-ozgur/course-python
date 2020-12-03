str_n = input("please enter a number")
n = int(str_n)
print(n)
d = 2
while d < n:
    print(d)
    if n % d == 0:
        print(f"number {n} is NOT a prime number")
    d = d + 1
#else:
#    print(f"number {n} is a prime number")
