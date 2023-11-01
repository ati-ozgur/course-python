## function title case

Write a function that give title case for an input.
For example given full names below, output will be capitalized as only first char.

if your function works, following asserts should work.

	def title_case(word):
	    # write code here
	    
	assert title_case("atilla ozgur") == "Atilla Ozgur"
	assert title_case("atiLLa ozgur") == "Atilla Ozgur"
	assert title_case("Atilla Ozgur") == "Atilla Ozgur"
 
	assert title_case("ATILLA OZGUR") == "Atilla Ozgur"
	assert title_case("AtiLLA OZGur") == "Atilla Ozgur"


