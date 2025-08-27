''' Write a function count_vowels(text, vowels="aeiou") that counts how many vowels appear in a given text.
  Example: count_vowels("Python is fun") should return 3. '''

vowel_list = []

def count_vowels(text, vowels = "aeiou"):
	flag = False
	for vowel in text:
		if vowel in vowels:
			vowel_list.append(vowel)
			flag = True
		
	else:
		if flag == False:
			print("Vowel Not Found!")

count_vowels("Python is fun")
print(len(vowel_list))

