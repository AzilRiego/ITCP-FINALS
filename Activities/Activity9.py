age = eval(input("Please enter your age: "))
	if age >= 1 and age <= 7:
		print("You're a toddler")
	elif age >= 8 and age<= 13:
		print("You're a preteen")
	elif age >= 14 and age<= 18:
		print("You're a teenager")
	elif age >= 19 and age<= 31:
		print("You're an early adult")
	elif age >= 32 and age<= 45:
		print("You're a mid adult")
	elif age >= 46 and age<= 59:
		print("You're a post adult")
	elif age >= 60 and age <= 100:
		print("You're a senior")
	else:
		print("Invalid Age, please try again")
