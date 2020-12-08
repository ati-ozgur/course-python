def encode_in_ceaser_cipher(text):
	encoded = ""
	for ch in text:
		v = ord(ch) - 65
		v = (v + 3) % 26
		v = v + 65
		new_ch = chr(v)
		encoded = encoded + new_ch
	return encoded



text = "ABC"
encoded_text = encode_in_ceaser_cipher(text)
print("text",text,"encoded_text", encoded_text)


text = "XYZ"
encoded_text = encode_in_ceaser_cipher(text)
print("text",text,"encoded_text", encoded_text)

text = "XYZ"
encoded_text = encode_in_ceaser_cipher(text)
print("text",text,"encoded_text", encoded_text)

text = "ATILLAOZGUR"
encoded_text = encode_in_ceaser_cipher(text)
print("text",text,"encoded_text", encoded_text)
