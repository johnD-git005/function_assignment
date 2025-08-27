''' Write a function count_even(numbers) that counts how many even numbers are in a list.
Example: count_even([1, 2, 3, 4, 6]) → 3 '''

new_even = []

def count_even(numbers):
	flag = False
	for num in numbers:
		if num % 2 == 0:
			new_even.append(num)
			flag = True
	else:
		if flag == False:
			print("Even Number Not Found!")

count_even([1, 2, 3, 4, 6])
print(len(new_even))
