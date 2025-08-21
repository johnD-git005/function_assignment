''' Write a function count_vowels(text, vowels="aeiou") that counts how many vowels appear in a given text.
  Example: count_vowels("Python is fun") should return 3. '''

vowels = "aeiou"
word = input("Enter Text: ").lower()
vowel_list = []

def count_vowels():
	flag = False

	for vowel in word:
		if vowel in vowels:
			vowel_list.append(vowel)
			continue
			flag = True 
	else:
		if flag:
			print("Vowel Not Found!")

count_vowels()
print(len(vowel_list))
