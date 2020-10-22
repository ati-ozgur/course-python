
with open("wikipedia-germany.txt", "rt", encoding="utf-8") as f:
	file_content = f.read()

word_list = file_content.split(" ")

# cleaning words

#print(word_list[0:100])

frequency_words = {}

for word in word_list:
	#  b = b + 1
	frequency_words[word] = frequency_words[word] + 1

