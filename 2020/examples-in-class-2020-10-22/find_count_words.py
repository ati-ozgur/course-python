
with open("wikipedia-germany.txt", "rt", encoding="utf-8") as f:
	file_content = f.read()

word_list = file_content.split(" ")

# cleaning words should be here but not in this example

frequency_words = {}

for word in word_list:
	if word in frequency_words:
		frequency_words[word] = frequency_words[word] +1
	else:
		frequency_words[word] = 1



# taken from
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
for w in sorted(frequency_words, key=frequency_words.get, reverse=True):
    print(w, frequency_words[w])

