import os
import time
menu = True

def balik():
    while menu:
        back = input("Do you wish to return? (Yes/No): ")
        if back.lower() == "yes":
            break
        else:
            os.system('cls')
            print("...")
            time.sleep(2)
            print("\nApologies, but you can't stay here.")
            time.sleep(2)
            print('')
            print("I'll be the one who'll get in trouble if you stay here longer than you should be.")
            time.sleep(5)
            break
                
def go():
    print("")
    input("Press Enter To Proceed.")

def learn_docstrings():
    time.sleep(2)
    print("A DOCSTRING is a special string used to document Python modules, classes, functions, or methods.")
    time.sleep(2)
    print("\nIt provides an explanation of what the code does,")
    os.system('cls')
    time.sleep(2)
    print("\nIt provides an explanation of what the code does, its purpose,")
    os.system('cls')
    time.sleep(2)
    print("\nIt provides an explanation of what the code does, its purpose, and sometimes details about parameters and return values.
   ")
    print("They are enclosed in triple quotes (\"\"\" or ''') and are usually the first statement in a function, class, or module.")
    input("\nPress Enter to Proceed.")

    # Step 1: Example of a Docstring
    def example_function():
        """
        This is a sample docstring.
        It describes what the function does.
        """
        print("This is a simple function with a docstring!")

    print("\nHere’s the code for the function:")
    print("""
def example_function():
    \"""
    This is a sample docstring.
    It describes what the function does.
    \"""
    print("This is a simple function with a docstring!")
    """)

    print("\nWhen you call the function, it behaves normally:")
    example_function()

    go()

    print("\nYou can view a function's docstring using the __doc__ attribute.")
    print("For example: example_function.__doc__")
    print("\nThe docstring for example_function is:")
    print(example_function.__doc__)

    go()

    print("\nWhy use docstrings?")
    time.sleep(2)
    os.system('cls')
          
    print("Improved readability:")
    time.sleep(2)
    print(" Helps others (and your future self) understand the purpose and usage of your code.")
    time.sleep(2)
    os.system('cls')
    print("Standardized documentation:")
    time.sleep(2)
    os.system('cls')
    print("Many tools, like Sphinx, can automatically generate documentation from docstrings.")
    time.sleep(2)
    os.system('cls')
    print("Accessible in runtime:")
    time.sleep(2)
    os.system('cls')
    print("Developers can view docstrings without referring to external documentation.")
    

    go()

    print("\nNow it's your turn! Write a simple function with a docstring.")
    print("Example:")
    print("""
def greet(name):
    \"""
    Greets the person with the given name.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        None
    \"""
    print(f"Hello, {name}!")
    """)

    print("\nTry writing and testing your own function in a Python environment!")

    print("\nKnowledge Acquired: Python Docstrings.")
    balik()

def learn_lists():
    print("In Python, a list is a built-in data structure that is used to store a collection of items in a single variable."
    go()

    print("\nShall we create a list of fruits using LIST?")
    os.system('cls')
    print("Lets make a list of my favorite fruit")
    os.system('cls')
    print("Example: fruits = ['Orange', 'Grapes', 'Watermelon']")
    fruits = ['Orange', 'Grapes', 'Watermelon']
    print("")
    print(f"Here's a sample list: {fruits}")
    go()

    print("\nYou can access elements in a list using their index (starting from 0).")
    print("Example: fruits[0] will give you the first item.")
    index = int(input("Enter an index (0-2) to see the corresponding fruit: "))
    if 0 <= index < len(fruits):
        print("")
        print(f"The fruit at index #{index} is {fruits[index]}")
    else:
        print("Invalid index!")
    go()

    print("\nYou can add items to a list using the append() method.")
    new_fruit = input("Enter the name of a fruit to add to the list: ")
    fruits.append(new_fruit)
    print(f"Updated list of fruits: {fruits}")
    time.sleep(1)
    print("Should I try that fruit?")
    go()

    print("\nYou can remove items from a list using the remove() method.")
    remove_fruit = input("Enter the name of a fruit to remove from the list: ")
    if remove_fruit in fruits:
        print("")
        fruits.remove(remove_fruit)
        print(f"Updated list of fruits: {fruits}")
        time.sleep(1)
        print("I never liked that fruit anyway.")
    else:
        print(f"{remove_fruit} is not in the list!")
        time.sleep(1)
        print("What fruit have you eaten to have hallucinations?")
    go()

    print("\nYou can loop through a list to process each item.")
    print("Example: Print each fruit in the list one by one.")
    print("for fruit in fruits:")
    print("    print(f'-{fruit}')")

    print("\nFruits in the list:")
    for fruit in fruits:
        print(f"-{fruit}") 
    go()

    print("\nKnowledge Acquired: Lists in terms of Python.")
    time.sleep(2)
    print("Now I crave some fruit.")
    time.sleep(2)
    print("I'm hungry.")
    balik()

def learn_modules():
    print("Welcome to the Python Modules Learning Program!")
    print("\nModules are files containing Python code, such as functions or classes, that you can reuse.")
    print("Python comes with many built-in modules, and you can also create your own.")
    print("\nTo use a module, you import it using the 'import' keyword.")
    go()

    # Step 1: Using a Built-in Module
    print("\nLet's use the built-in 'math' module to perform calculations.")
    print("Import the 'math' module and use its 'sqrt()' function to calculate the square root.")
    import math
    num = float(input("Enter a number to find its square root: "))
    print(f"The square root of {num} is {math.sqrt(num)}")

    go()

    print("\nYou can also create your own module by saving Python code in a file.")
    print("For example, if you save the following code in 'mymodule.py':")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')")

    print("\nThen you can import it using:")
    print("import mymodule")
    print("mymodule.greet('Alice')")

    print("\nSince we can't create a file here, try creating a custom module on your own!")
    go()

    print("\nYou can import specific functions or variables from a module using:")
    print("from module_name import function_name")
    print("\nExample:")
    print("from math import pi")
    print("print(pi)")

    from math import pi
    print(f"\nThe value of pi is: {pi}")
    print("\nYou can now explore more modules and create your own!")
    print("Great job! You've learned the basics of Python modules.")
    balik()


def grades():
    prelim = int(input("Enter your score for the prelims: "))
    midterm = int(input("Enter your score for the midterms: "))
    semif = int(input("Enter your score for the semifinals: "))
    final = int(input("Enter your score for the finals: "))
    quiz  = int(input("Enter your score for the quizzes: "))
    project = int(input("Enter your score for the projects: "))

    FG = prelim * 0.15 + midterm * 0.15 + semif * 0.15 + final * 0.15 + quiz * 0.25 + project * 0.15 
    print("Your Final Grade issssss", end=" ")
    print(FG)
    if FG > 100:
        print("Aw you cheated, fail")
        print("Kaya mo yan")
        balik()
    elif FG >= 75:
        print("Pasado ka! Yey!")
        print("Good luck, keep it up!")
        balik()
    else:
        print("Welp, only way is up from here")
        balik()

def operations():
        number1 = eval(input("Enter a number: "))
        number2 = eval(input("Enter a second number: "))
        answer1 = number1 + number2
        answer2 = number1 - number2
        answer3 = number1 * number2
        answer4 = number1 / number2
        answer5 = number1 ** number2
        answer6 = number1 // number2
        answer7 = number1 % number2
        print("     [#1] Add")
        print("     [#2] Subtract")
        print("     [#3] Multiply")
        print("     [#4] Divide")
        print("     [#5] Floor Divide")
        print("     [#6] Exponent")
        print("     [#7] Modulo")
        ope = int(input("What do you want to do with the two numbers? (Enter just the number)\n"))
        if ope == 1:
            print("The sum of" , number1 , "and" , number2 , "is" , answer1)
        elif ope == 2:
            print("The difference of" , number1 , "and" , number2 , "is" , answer2)
        elif ope == 3:
            print("The product of" , number1 , "and" , number2 , "is" , answer3)
        elif ope == 4:
            print("The quotient of" , number1 , "and" , number2 , "is" , answer4)
        elif ope == 6:
            print(number1 , "exponent by" , number2 , "is" , answer5)
        elif ope == 5:
            print("The floor division of" , number1 , "and" , number2 , "is" , answer6)
        elif ope == 7:
            print("The remainder of" , number1 , "and" , number2 , "is" , answer7)
        else:
            print('INVALID INPUT. PLEASE TRY AGAIN')
    
def breakdown_denomination(amount):
    print("Denomination Breakdown:")
    denominations = (1000, 500, 200, 100, 50, 20, 10, 5, 1)
    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            print("PHP", denom, ":", count)
            amount = amount % denom


def create_account():
    account_name = input("Enter your name: ")
    initial_deposit = eval(input("Enter initial deposit: "))
    if initial_deposit >= 0:
        print("Account created for", account_name, "with balance PHP", initial_deposit)
        return account_name, initial_deposit
    else:
        print("Initial deposit must be 0 or more.")
        return None, 0


def deposit(account_name, account_balance):
    if account_name == None:  
        print("No account found. Please create an account first.")
    else:
        amount = eval(input("Enter amount to deposit: "))
        if amount > 0:
            account_balance += amount
            print("Deposited PHP", amount, ". Current balance: PHP", account_balance)
            breakdown_denomination(amount)
        else:
            print("Deposit amount must be greater than 0.")
    return account_balance


def withdraw(account_name, account_balance):
    if account_name == None:
        print("No account found. Please create an account first.")
    else:
        amount = eval(input("Enter amount to withdraw: "))
        if amount > account_balance:
            print("Insufficient balance!")
        elif amount > 0:
            account_balance -= amount
            print("Withdrew PHP", amount, ". Current balance: PHP", account_balance)
        else:
            print("Withdrawal amount must be greater than 0.")
    return account_balance


def check_balance(account_name, account_balance):
    if account_name == None:
        print("No account found. Please create an account first.")
    else:
        deposit = account_balance
        answer1 = deposit // 1000
        num1 = deposit % 1000
        answer2 = num1 // 500
        num2 = num1 % 500
        answer3 = num2 // 200
        num3 = num2 % 200
        answer4 = num3 // 100
        num4 = num3 % 100
        answer5 = num4 // 50
        num5 = num4 % 50
        answer6 = num5 // 20
        num6 = num5 % 20
        answer7 = num6 // 10
        num7 = num6 % 10
        answer8 = num7 // 5
        num8 = num7 % 5
        answer9 = num8 // 1
        print("Hi", account_name , ", the breakdown of your deposit is:")
        print(account_balance)
        print(answer1 , "- 1000")
        print(answer2 , "- 500")
        print(answer3 , "- 200")
        print(answer4 , "- 100")
        print(answer5 , "- 50")
        print(answer6 , "- 20")
        print(answer7 , "- 10")
        print(answer8 , "- 5")
        print(answer9 , "- 1")

def main():
    account_name = None
    account_balance = 0

    while True:
        print("\n=== Welcome to J-Bank ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            os.system('cls')
            account_name, account_balance = create_account()
        elif choice == "2":
            os.system('cls')
            account_balance = deposit(account_name, account_balance)
        elif choice == "3":
            os.system('cls')
            account_balance = withdraw(account_name, account_balance)
        elif choice == "4":
            os.system('cls')
            check_balance(account_name, account_balance)
        elif choice == "5":
            print("Thank you for using the banking system!")
            balik()
            break
        else:
            print("Invalid option. Please try again.")

def learn_functions():
    print("Welcome to the Python Functions Learning Program!")
    print("\nA function is a reusable block of code that performs a specific task.")
    print("You define a function in Python using the 'def' keyword.")
    print("\nExample:")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')")

    go()

    print("\nLet's create a custom function to greet someone.")
    print("Here’s how the function works:")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')")

    def greet(name):
        print(f"Hello, {name}!")

    name = input("\nEnter your name: ")
    greet(name)

    go()

    print("\nFunctions can take multiple parameters.")
    print("Example: def add_numbers(a, b):")
    print("             return a + b")

    print("\nLet's create a function to add two numbers.")
    
    def add_numbers(a, b):
        return a + b

    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

    go()

    print("\nFunctions can return values using the 'return' keyword.")
    print("This allows you to store the result of a function in a variable.")
    print("For example:")
    print("result = add_numbers(3, 5)")
    print("print(result)")

    print("\nTry calling the add_numbers function with different numbers!")
    print("Feel free to modify the code to experiment further.")

    print("\nGreat job! You've learned the basics of custom functions in Python.")
    balik()



def Initialize():
    os.system('cls')
    print("Initializing.")
    time.sleep(0.5)
    os.system('cls')
    print("Initializing..")
    time.sleep(0.5)
    os.system('cls')
    print("Initializing...")
    time.sleep(0.5)
    os.system('cls')

def LoadingScreen_Long():
    # Clear screen and start loading process
    os.system('cls')
    time.sleep(1)

    # First loading step
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t█')
    time.sleep(1)

    # Clear screen for the second loading step
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t█████')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t███████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t███████████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t████████████████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t████████████████████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1) 

    os.system('cls')
    print("\t\t\t\t\t\t\t\t")
    print('\t\t\t\t\t\t\t     Program Ready!')

def LoadingScreen_Short():
    # Clear screen and start loading process
    os.system('cls')
    time.sleep(1)

    # First loading step
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t████')
    time.sleep(1)

    # Clear screen for the second loading step
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t███████')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t███████████████')
    print("\t\t\t\t\t\t\t   No man's an island!")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t█████████████████████')
    print("\t\t\t\t\t\t\t   No man's an island!")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t████████████████████████')
    print("\t\t\t\t\t\t\t   No man's an island!")
    time.sleep(1) 

    os.system('cls')
    print("\t\t\t\t\t\t\t\t")
    print('\t\t\t\t\t\t\t     Program Ready!')

def LoadingScreen_Short2():
    # Clear screen and start loading process
    os.system('cls')
    time.sleep(1)

    # First loading step
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t██')
    time.sleep(1)

    # Clear screen for the second loading step
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t████')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t█████████')
    print("\t\t\t\t\t\t\tIt's going to be alright")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t█████████████')
    print("\t\t\t\t\t\t\tIt's going to be alright")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t████████████████')
    print("\t\t\t\t\t\t\tYou'll do great things")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t███████████████████')
    print("\t\t\t\t\t\t\tYou'll do great things")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t█████████████████████')
    print("\t\t\t\t\t\t\t       Stand Proud")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t████████████████████████')
    print("\t\t\t\t\t\t\t       Stand Proud")
    time.sleep(1) 

    os.system('cls')


#THIS IS WHERE THE PROGRAM TRULY STARTS
time.sleep(1) 
LoadingScreen_Long()
os.system('cls')
time.sleep(1)
print("Welcome!")
print(" ")
time.sleep(1)
print("This'll serve as my(James Miro R. Orte) compilation of works and")
time.sleep(2)
print("culmination of learnings throughout my 1st Semester at DLL!")
print(" ")
time.sleep(2)
print("So without further ado...")
time.sleep(1)
print("please enjoy browsing through all my work!")
time.sleep(2)
LoadingScreen_Short()

print("Let's start off with the basics!")
time.sleep(1.5)
while menu:
    os.system('cls')
    print("")
    print("")
    print("               █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    print("               █========================▶ THE MENU ◀==========================█")
    print("               █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    print("               █    [#1] Greet Yourself!         [#11] Triangle Mania!        █")
    print("               █    [#2] Easy-Peasy Biodata!     [#12] Grade Calculator!      █")
    print("               █    [#3] Guess the Password!     [#13] Supermarket Sim!       █")
    print("               █    [#4] Convert C° to F°!       [#14] Banking System!        █")
    print("               █    [#5] Assignment Operators!   [#15] Lists!                 █")
    print("               █    [#6] Gold Miner!             [#16] Modules!               █")
    print("               █    [#7] Your Age Group!         [#17] Custom Functions!      █")
    print("               █    [#8] Scholarship Grant!      [#18] Document Strings!      █")
    print("               █    [#9] Loops!                                               █")
    print("               █    [#10] Factorials!            [#0] Exit                    █")
    print("               █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    choice = int(input("So, what would you like to try? (Enter just the 'number' to the corresponding task)\n"))
    if choice == 1:
        os.system('cls')
        time.sleep(1)
        Initialize()
        os.system('cls')
        print("Welcome! This project will greet any and all names you put in it!")
        time.sleep(2)
        print("")
        print("Why not give it a try?")
        time.sleep(1)
        name = input("Please enter a name! ---> ")

        print(f"Hi {name}!")
        time.sleep(2)
        print("")
        print("Pretty fun wasn't it?")
        time.sleep(1)
        print("")
        print("Now go back and try the other fun options!")
        balik()
        continue
    elif choice == 2:
        Initialize()
        os.system('cls')
        time.sleep(1)
        print("Welcome to your very own Biodata Maker! ")
        time.sleep(1)
        print("")
        print("Just fill in the information asked and it'll do it for you")
        time.sleep(1)
        print('')
        print("Neat, ain't it?")
        time.sleep(1)
        os.system('cls')
        full_name = input("Please enter your full name: ")
        gender = input("Please enter your gender: ")
        age = input("Please enter your age: ")
        Fname = input("Please enter your father's full name: ")
        Mname = input("Please enter your mother's maiden name: ")
        nationality = input("Enter you nationality: ")
        birthdate = input("Enter your date of birth: ")
        birthplace = input("Enter your place of birth: ")
        civil_status = input("Enter your civil status: ")
        religion = input("Enter you religion: ")
        skills = input("Enter your relevant skills: ")
        hobbies = input("Enter your hobbies: ")
        email_address = input("Please enter a valid e-mail address: ")
        mobile_no = input("Please enter your mobile number: ")
        print("Hi! I'm " , full_name , "\b.I am" , gender , "and I am" , age , "years old. My parents are" , Fname , "and" , Mname, "\b. I am" , nationality , "and was born on", birthdate , "at" , birthplace , "and am currently" , civil_status,"\b. My religion is" , religion , "and I am proficient in" , skills , "and not only that but I also like to do" , hobbies , "in my free time. If you have any more questions about me you can contact me through" , email_address , "or" , mobile_no , "\b, and that's all about me. Thank you!")
        time.sleep(1)
        print('')
        ilu = input("So, did you like it? (Y/N): ")
        print('')
        print("Cool, now go and try the others!")
        balik()
        continue
    elif choice == 3:
        Initialize()
        password = input("Please enter a password ----> ")
        if password.lower() == "secret066":
            print("May tama ka!")
            print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
            balik()
        elif password == "jamesorte":
            print("Well tama rin")
            print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
            balik()
        else:
            print("Nope, try again")
            print("Hint: First & Last name of author")
            balik()
        print("Thank you for choosing Globe, as your number one service provider!")
        time.sleep(2)
        continue
    elif choice == 4:
        Initialize()
        print("Farenheit to Celsius Converter Program!")
        time.sleep(1)

        fahrenheit = eval(input("Please enter temperature in Farenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The conversion of" , fahrenheit , "degrees Fahrenheit is" , round(celsius,2) , "degrees Celcius!")
        time.sleep(2)
        input("Get it? (Y/N)")
        continue
    elif choice == 5:
        x = 5
        Initialize()
        print("Welcome to a guide to ASSIGNMENT Operators!")
        time.sleep(1)
        print("")
        print("Let's say x = 5")
        print("")
        time.sleep(2)
        print("Then say we do: x = x + 10")
        x = x + 10
        time.sleep(2)
        print("We added 10 to x so our total would now amount to:", x)
        time.sleep(2)
        print("")
        print("Let's try adding another:")
        time.sleep(1)
        print("x = x + 15")
        x = x + 15
        time.sleep(2)
        print("")
        print("Our total would now amount to ", x)
        time.sleep(3)
        os.system('cls')
        print("By using these assignment operators")
        time.sleep(1)
        print("We can use these to do basic operations on numeric values")
        print('')
        time.sleep(1)
        print("                                            >List of Operations<")
        print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
        print("                                     █   = - Assigns values            █")
        print("                                     █   + or += Adds two values       █")
        print("                                     █   - or -= Subtracts two values  █")
        print("                                     █   * or *= Multiplies two values █")
        print("                                     █   / or /= Divides two values    █")
        print("                                     █   // or //= Divides floor value █")
        print("                                     █   % or %= Gives the remainder   █")
        print("                                     █   ** or **= Raises exponent     █")
        print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
        print("Have a go with it!")
        time.sleep(1)
        operations()
        print("")
        input("Easy, right? (Y/N): ")
    elif choice == 6:
        os.system('cls')
        Initialize()
        name = input("What's your name?: ")
        tot = 0
        ans = input(f"So {name},have you mined today? (Y/N):  ")
        print("\n")
        if ans.upper() == "Y": #main operation if "yes"
            gold = eval(input("How much Gold did you mine (Number)? "))
            all = tot + gold
            print(f"Good day {name}, you have mined {all} gold today!")
            time.sleep(2)
        elif ans.upper() != "Y": #sub operation if "no"
            print("Then go mine some", name )
            time.sleep(2)
        else:
            print("Huh?")
            time.sleep(2)
        pass
    elif choice == 7:
        Initialize()
        print("Find out your age with a press of a button!")
        age = eval(input("Please enter your age: "))
        if age >= 1 and age <= 7:
            print("You're a toddler")
            input("Go back (Y/N)? ")
        elif age >= 8 and age<= 13:
            print("You're a preteen")
            input("Go back (Y/N)? ")
        elif age >= 14 and age<= 18:
            print("You're a teenager")
            input("Go back (Y/N)? ")
        elif age >= 19 and age<= 31:
            print("You're an early adult")
            input("Go back (Y/N)? ")
        elif age >= 32 and age<= 45:
            print("You're a mid adult")
            input("Go back (Y/N)? ")
        elif age >= 46 and age<= 59:
            print("You're a post adult")
            input("Go back (Y/N)? ")
        elif age >= 60 and age <= 100:
            print("You're a senior ")
            input("Go back (Y/N)?")
        else:
            print("Tanda mo naman")
            input("Go back (Y/N)? ")
       
    elif choice == 8:
        Initialize()
        isDLL = input("Are you currently enrolled in DLL?(Y/N): ")
        if isDLL.lower() == "y":
            isIYAM = input("Do you currently live in Brgy. Ibabang Iyam?(Y/N): ")
            if isIYAM.lower() == "y":
                print("Welcome! Please confirm your school year")
                print("F - Freshman")
                print("S - Sophomore")
                print("J - Junior")
                print("R - Senior")
                isSY = input("Please enter your current year level in DLL:")
                if isSY.lower() == "f":
                    print("Hi Freshman!")
                elif isSY.lower() == "s":
                    print("Hi Sophomore!")
                elif isSY.lower() == "j":
                    print("Hi Junior!")
                elif isSY.lower() == "r":
                    print("Hi Senior!")
                else:
                    print("Invalid year level, please try again")
                isScho = input("Do you need this scholarship?(Y/N): ")
                if isScho.lower() == "y":
                    print("You have been granted a full scholarship, thank you for choosing DLL")
                    balik()
                else:
                    print("Okay, have a nice day")
                    balik()
            else:
                print("Sorry, you are not eligible")
                balik()
        else:
            print("Sorry, you are not eligible")
            balik()
    elif choice == 9:
        Initialize()
        print("Welcome to loops! Using the loop function")
        print("we can repeat a code block as many times we want")
        time.sleep(1)
        print()
        print("It should look like this:")
        print("for x in range(Starting_Point,Stopping_Point, Increment/Decrement):")
        go()
        print('')
        print("So let's say:")
        print("for x in range(1,11):")
        print("     print('Hello World')")
        go()
        os.system('cls')
        print("It should look like this:")
        time.sleep(1)
        for x in range(1,11):
            print("     Hello World")
        time.sleep(1)
        print('Neat!')
        balik()
    elif choice == 10:
        Initialize()
        print("Welcome. You can factorial any number here!")
        factorial = 1
        print("")
        start = eval(input("So, enter the number you want to factorial: "))
        for x in range(start,0,-1):
            print(x)
            factorial *= x
        print(f"the factorial of {start} is {factorial} ")
        time.sleep(1)
        print("Neat")
        balik()
    elif choice == 11:
        Initialize()
        print("Now let's utilize loops to make some neat shapes!")
        time.sleep(2)
        print("Let's utilize this code block to create a simple triangle:")
        print(" ")
        print("for x in range(1,6):")
        print("      print('* ' * x)")
        print("")
        go()
        print("And, it should look like this")
        for x in range(1,6):
            print('* ' * x)
        print("")
        print("Now go and try the others!")
        go()
        while menu:
            os.system('cls')
            print("                                            >Triangles & Others<")
            print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
            print("                                     █   [#1] Diamond                  █")
            print("                                     █   [#2] An Arrow                 █")
            print("                                     █   [#3] Number Rhombus           █")
            print("                                     █   [#4] Upside-down Pyramid      █")
            print("                                     █   [#5] Main Menu                █")
            print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
            print("Have a go with it!")
            option = int(input("Enter the number of the shape you want to see:"))
            if option == 1:
                os.system('cls')
                for x in range(1, 6):
                    for y in range(6,x,-1):
                        print(" ",end=" ")
                    for z in range(1,x+1):
                        print("*",end=" ")
                    for a in range(1,x+1):
                        print("*",end=" ")
                    print()
                for x in range(1, 6):
                    for y in range(1,x+1):
                        print(" ",end=" ")
                    for z in range(6,x,-1):
                        print("*",end=" ")
                    for a in range(6,x,-1):
                        print("*",end=" ")
                    print()
                go()
            elif option == 2:
                    os.system('cls')
                    for x in range(1, 5):
                        for y in range(6,x,-1):
                            print(" ",end=" ")
                        for z in range(1,x+1):
                            print("*",end=" ")
                        for a in range(1,x+1):
                            print("*",end=" ")
                        print()

                    for x in range(1, 6):
                        for y in range(1,6):
                            print(" ",end=" ")
                        for z in range(1,3):
                            print("*",end=" ")
                        print()
                    go()
            elif option == 3:
                os.system('cls')
                for x in range(1, 7):
                    for y in range(6,x,-1):
                        print(" ",end=" ")
                    for z in range(x,1,-1):
                        print(z,end=" ")    
                    for a in range(1,x+1):
                        print(a,end=" ")
                    print()

                for x in range(5, 0,-1):
                    for y in range(6,x,-1):
                        print(" ",end=" ")
                    for z in range(x,1,-1):
                        print(z,end=" ")
                    for a in range(1,x+1):
                        print(a,end=" ")
                    print()
                go()
            elif option == 4:
                os.system('cls')
                t = int(input("Enter a number range: "))
                for x in range(1,t):
                    for a in range(1,x,1):
                        print(" ",end="  ")
                    for b in range(t,x,-1):
                        print("^ ",end=" ")   
                    for b in range(t,x,-1):                            
                        print("* ",end=" ")        
                    print()  
                go()
            elif option == 5:
                break
            else:
                print("INVALID INPUT. PLEASE TRY AGAIN")
                continue

    elif choice == 12:
        Initialize()
        grades()
    elif choice == 13:
            Initialize()
            name = input("Enter your name: ")
            print("")
            age = int(input("Enter your age: "))
            print()
            print("\nPlease select from these items:")
            print("1. Lamb: 350")
            print("2. Sirloin: 450")
            print("3. Caviar: 1000")
            print("4. Truffle Oil: 1200")
            print("5. Foie Gras: 800")
            print("Enter '0' when you are done selecting items.")

            total = 0

            while True:
                item = int(input("\nEnter the number of the item you want to buy (or 0 to finish): "))
                if item == 1:
                    total += 350
                elif item == 2:
                    total += 450
                elif item == 3:
                    total += 1000
                elif item == 4:
                    total += 1200
                elif item == 5:
                    total += 800
                elif item == 0:
                    break
                else:
                    print("Invalid selection. Please choose a valid number.")

            if total == 0:
                print("You didn't buy anything.")

            tax_percentage = 15
            discount_percentage = 10

            tax = (total * tax_percentage) / 100
            total_with_tax = total + tax
            print(f"\nA tax of {tax_percentage}% is added, which is {tax:.2f}.")

            if age >= 60:
                discount = (total_with_tax * discount_percentage) / 100
                print(f"\nYou get a discount of {discount_percentage}% which is {discount:.2f}.")
                total_with_tax -= discount

            print(f"Your total amount is: {total_with_tax:.2f}")

            confirm = input(f"\n{name}, do you accept the charges? (yes/no): ")
            if confirm == "yes":
                print("Thank you for your purchase!")
                balik()
            else:
                print("Purchase cancelled.")
                balik()

    elif choice == 14:
        Initialize()
        main()
    elif choice == 15:
        Initialize()
        learn_lists()
    elif choice == 16:
        Initialize()
        learn_modules()
    elif choice == 17:
        Initialize()
        learn_functions()
    elif choice == 18:
        Initialize()
        learn_docstrings()
    elif choice == 0:
        os.system('cls')
        time.sleep(2)
        print("Thank you for using my project!")
        time.sleep(2)
        print("Even if you just browsed through a little bit or went through everything")
        time.sleep(3)
        print("I want to thank you for going through the effort of seeing it through")
        time.sleep(2)
        print("And that effort, the work you put into things no one else will ever see")
        time.sleep(2)
        print("It'll be worth it. I promise")
        time.sleep(2)
        print("Keep being you, because the worst mistake you can make is not being yourself")
        time.sleep(3)
        print("And NEVER let anyone say otherwise")
        time.sleep(2)
        print("So...")
        time.sleep(2)
        print("Thank you.")
        print("")
        time.sleep(2)
        print("One more thing, a little something just for you")
        time.sleep(2)
        input('Enter anything to continue (Full screen your terminal for this one): ')
        os.system('cls')
        LoadingScreen_Short2()
        print("It's ready")
        time.sleep(2)
        print("Last one, I promise")
        time.sleep(4)
        os.system('cls')
        print("  ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .")
        time.sleep(0.5)
        print("      ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :")
        time.sleep(0.5)
        print("         .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.")
        print("                `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|")
        time.sleep(0.5)
        print("        *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||")
        print("             .`            | |  |  : .:|       ` | || | : |: |          | ||")
        time.sleep(0.5)
        print("      '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||")
        print("         .                 .    ` *|  || :       `    | | :| | :      |:| |")
        print(" .                .          .        || |.: *          | || : :     :|||")
        time.sleep(0.5)
        print("        .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`")
        print("     .             *              .     +:`|!             . ||||  :.||`")
        print(" +                      .                ..!|*          . | :`||+ |||`")
        time.sleep(0.5)
        print("     .                         +      : |||`        .| :| | | |.| ||`     .")
        print("       *     +   '               +  :|| |`     :.+. || || | |:`|| `")
        time.sleep(0.5)
        print("                            .      .||` .    ..|| | |: '` `| | |`  +")
        print("  .       +++                      ||        !|!: `       :| |")
        print("              +         .      .    | .      `|||.:      .||    .      .    `")
        time.sleep(0.5)
        print("          '                           `|.   .  `:|||   + ||'     `")
        print("  __    +      *                         `'       `'|.    `:")
        print("\"'  `---\"\"\"----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-")
        print("    ___,--'\"\"`---\"'   ^  ^ ^        ^       \"\"\"'---,..___ __,..---\"\"'")
        time.sleep(0.5)
        print("--\"'                           ^                         ``--..,__ ")
        print("                                   /\\")
        print("                              /\\  //\\\\")
        time.sleep(0.5)
        print("                       /\\    //\\\\///\\\\\\        /\\")
        print("                      //\\\\  ///\\////\\\\\\\\  /\\  //\\\\")
        print("         /\\          /  ^ \\/^ ^/^  ^  ^ \\/^ \\/  ^ \\")
        time.sleep(0.5)
        print("        / ^\\    /\\  / ^   /  ^/ ^ ^ ^   ^\\ ^/  ^^  \\")
        print("       /^   \\  / ^\\/ ^ ^   ^ / ^  ^    ^  \\/ ^   ^  \\       *")
        print("      /  ^ ^ \\/^  ^\\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \\     /|\\")
        time.sleep(0.5)
        print("     / ^ ^  ^ \\ ^  _\\___________________|  |_____^ ^  \\   /||o\\")
        print("    / ^^  ^ ^ ^\\  /______________________________\\ ^ ^ \\ /|o|||\\")
        print("   /  ^  ^^ ^ ^  /________________________________\\  ^  /|||||o|\\")
        time.sleep(0.5)
        print("  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\\       |")
        print(" / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |")
        print("/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  |")
        time.sleep(0.5)
        print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        print("")
        time.sleep(2)
        print("Scenery's nice this time of year...")
        time.sleep(3)
        end = input("Shall we go? We have our whole lives ahead of us (Y/N): ")
        if end.lower() == "y":
            os.system('cls')
            print("Until we meet again!")
            time.sleep(2)
            print("Don't be too hard on yourself for me, okay?")
            time.sleep(3)
            print("PROGRAM TERMINATED")
            break
        else:
            print("")
            print("Alright...")
            time.sleep(2)
            print("Just a little bit longer...")
            time.sleep(2)
            print('')
            input("Just enter anything when you're ready: ")
            os.system('cls')
            print("Until we meet again!")
            time.sleep(2)
            print("Don't be too hard on yourself for me, okay?")
            time.sleep(3)
            print("PROGRAM TERMINATED")
            break
    else:
        print("None of the options were chosen. Try again")
        continue
