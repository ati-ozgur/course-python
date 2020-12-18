def find_digits(num):
    l = []
    while num > 0:
        digit = num % 10 
        num = num // 10
        l = [digit] + l
    return l
    
    


print(find_digits(100))
print(find_digits(987))
print(find_digits(121))
print(find_digits(34543))
print(find_digits(4567))