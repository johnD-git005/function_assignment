''' Write a function check_even_odd(n) that takes an integer n and returns:
"Even" if the number is even,
"Odd" if the number is odd. '''

def check_even_odd(n):
	if n % 2 == 0:
		print("Even Number")
	else: 
		print("Odd Number")

number = int(input("Enter a Number: "))
check_even_odd(number)
