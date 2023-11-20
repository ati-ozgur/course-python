## Question -- ordinal suffix writing

Paraphrased from [wikipedia](https://en.wikipedia.org/wiki/Ordinal_numeral)

> Ordinal numbers may be written in English with numerals and letter suffixes: 1st, 2nd, 3rd, 4th, 11th, 21st, 101st, 477th, etc., with the suffix acting as an ordinal indicator.

Write a function, named get_ordinal_suffix which have a single parameter named num.
This function will return a string containing both num and suffix.
Rules like below:

	- last two digits are 11,12,13 then suffix is "th"
	- last digit is 1 then suffix is "st"
	- last digit is 2 then suffix is "nd"
	- last digit is 3 then suffix is "rd"
	- for every other number, suffix is "th"



If your function is correct, below asserts should work without error.

```python
assert get_ordinal_suffix(1) == "1st"
assert get_ordinal_suffix(2) == "2nd"
assert get_ordinal_suffix(3) == "3rd"
assert get_ordinal_suffix(11) == "11th"
assert get_ordinal_suffix(12) == "12th"
assert get_ordinal_suffix(13) == "11th"
assert get_ordinal_suffix(21) == "21st"
assert get_ordinal_suffix(22) == "22nd"
assert get_ordinal_suffix(33) == "33rd"
assert get_ordinal_suffix(101) == "3rd"

assert get_ordinal_suffix(1000) == "1000th"

```

1000st








