value = input("Please enter a input to test for palindrome:")
#value = "hannah"

is_palindrome = True
for index in range(len(value)):
    reverse_index = len(value) - index-1
    char_from_start = value[index]
    char_from_end = value[reverse_index] 
    #print(char_from_start,char_from_end )
    if char_from_start != char_from_end:
        is_palindrome = False

if is_palindrome:
    print(f"{value} is a palindrome")
else:
    print(f"{value} is NOT a palindrome")


