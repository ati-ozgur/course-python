def find_digits(num):
    l = []
    while num > 0:
        digit = num % 10 
        num = num // 10
        l = [digit] + l
    return l
    
    

def is_palindrome(num):
    digits = find_digits(num)
    count = len(digits)
    for i in range(count):
        d1 = digits[i]
        d2 = digits[count-1-i]
        #print(d1,d2)
        if  d1 != d2:
            return False
    

    return True


#numbers = [121,3443,34543,321,4567,123421]

#for num in numbers:
#    print(num,is_palindrome(num))


s = input("Please enter a number to test:")
num = int(s)
if is_palindrome(num):
    print(f"Number {num} is a Palindrome.")
else:
    print(f"Number {num} is not a Palindrome.")

