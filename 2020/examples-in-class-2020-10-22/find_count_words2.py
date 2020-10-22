
with open("wikipedia-germany.txt", "rt", encoding="utf-8") as f:
	file_content = f.read()

word_list = file_content.split(" ")

# cleaning words

#print(word_list[0:100])

frequency_words = {}

for word in word_list:
	# does not work since we are trying to get value of something which does not exist
	# it is similar to below line if b is not defined.
	#  b = b + 1	
	frequency_words[word] = frequency_words[word] + 1

