''' Write a function count_even(numbers) that counts how many even numbers are in a list.
Example: count_even([1, 2, 3, 4, 6]) → 3 '''

even = [1, 2, 3, 4, 6]
new_even = []

def count_even():

	for num in even:
		if num % 2 == 0:
			new_even.append(num)
count_even()
print(len(new_even))
