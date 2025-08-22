''' Write a function called check_password_strength that takes a password string and returns "Weak", "Medium", or "Strong" based on these criteria: Weak (less than 6 characters), Medium (6-10 characters), Strong (more than 10 characters and contains both letters and numbers).'''

password = input("Enter Password \n Password must contain both letters and numbers: ")

def check_password_strength():

	if " " in password:
		print("\n Invalid Password! spaces are not allowed")

	elif not password or password == "":
		print("\n Password cannot be empty!") 	

	elif password.isalpha():
		print("\n Password must contain at least a Number")

	elif password.isdigit():
		print("\n Password must contain at least a Letter!")

	elif len(password) < 6:
		print("\n Password Strength: Weak")

	elif len(password) >= 6 and len(password) <= 10:
		print("\n Password Strength: Medium")

	elif len(password) > 10:
		print("\n Strong Password!")

	else:
		pass

check_password_strength()
