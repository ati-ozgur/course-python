
input_str = "12233227"

middle_size = int(round(len(input_str) / 2) )

print(f"middle_size:  {middle_size}")

end_index = -1
start_index = 0
while start_index < middle_size:
    char_from_start = input_str[start_index]
    char_from_end = input_str[end_index]
    end_index = end_index - 1
    start_index = start_index + 1
    if(char_from_end == char_from_start):
        continue
    else:
        print(f"input string {input_str} is not a palindrome")
        break
else:
    print(f"input string {input_str} is a palindrome")


