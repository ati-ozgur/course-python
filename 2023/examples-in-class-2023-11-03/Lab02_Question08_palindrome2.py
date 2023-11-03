value = input("Please enter a input to test for palindrome:")
#value = "hannah"

# reversing string here
reverse = value[::-1]

is_palindrome = reverse == value

if is_palindrome:
    print(f"{value} is a palindrome")
else:
    print(f"{value} is NOT a palindrome")


