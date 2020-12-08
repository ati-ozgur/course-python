def encode_in_ceaser_cipher(text):
	encoded = ""
	for ch in text:
		v = ord(ch)
		v = v + 3
		new_ch = chr(v)
		encoded = encoded + new_ch
	return encoded



text = "ABC"
encoded_text = encode_in_ceaser_cipher(text)
print(encoded_text)


text = "XYZ"
encoded_text = encode_in_ceaser_cipher(text)
print(encoded_text)
