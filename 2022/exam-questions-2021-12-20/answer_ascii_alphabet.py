
print(ord("A"))
print(chr(65))

print(ord("Z"))
print(chr(90))

print(ord("a"))
print(chr(97))

print(ord("z"))
print(chr(122))


for ascii_number in range(ord("A"),ord("Z")+1):
    ascii_char = chr(ascii_number)
    print(f"ascii number: {ascii_number}, ascii char: {ascii_char}")

for ascii_number in range(ord("a"),ord("z")+1):
    ascii_char = chr(ascii_number)
    print(f"ascii number: {ascii_number}, ascii char: {ascii_char}")