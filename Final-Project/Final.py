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
    print("\nIt provides an explanation of what the code does, its purpose, and sometimes details about parameters and return values.")
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
    print("In Python, a list is a built-in data structure that is used to store a collection of items in a single variable.")
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
            print("Deposited: ", amount, ". Current balance: ", account_balance)
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
            print("Withdrew: ", amount, ". Current balance: ", account_balance)
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
        print("\nCyber's Bank")
        time.sleep(2)
        print("Sadly, these aren't real money.")
        time.sleep(1)
        print("1. Create Account")
        time.sleep(1)
        print("2. Deposit")
        time.sleep(1)
        print("3. Withdraw")
        time.sleep(1)
        print("4. Check Balance")
        time.sleep(1)
        print("5. Exit")
        time.sleep(10)
        print("6. Rob")
        time.sleep(1)
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
            print("Thank you for emptying the creator's wallet.")
            time.sleep(1)
            os.system('cls')
            print("I mean thank you for using Cyber's Bank!")
            balik()
            break
        elif choice == "6":
            print("I can't let you do that.")
            time.sleep(1)
            print("Security.")
            break
        else:
            print("Invalid option. Please try again.")

def learn_functions():
    print("What is a Function?")
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



def Wait():
    os.system('cls')
    print("Please Wait.")
    time.sleep(0.5)
    os.system('cls')
    print("Please Wait..")
    time.sleep(0.5)
    os.system('cls')
    print("Please Wait...")
    time.sleep(0.5)
    os.system('cls')


#Start Point
time.sleep(1) 
os.system('cls')
time.sleep(1)
print("Howdy!")
time.sleep(1)
print("This project was brought to you by:")
time.sleep(1)
print("Azil Nheecolle Riego")
time.sleep(1)
print("From BSIT-1A")
time.sleep(5)
os.system('cls')
print("I named this program: 'Cyber'.")
time.sleep(2)
print("It is programmed to teach you the basic knowledge of the Python languange")
time.sleep(2)
print("I'll leave you to it's care!")
time.sleep(2)
print("Fear not, it can't harm you or anything...")

Wait()

print("Greetings and Salutations! Would you like to try my creator's practices in coding? It may help you out if you're a beginner.")
time.sleep(1.5)
while menu:
    os.system('cls')
    print("")
    print("1. 'Hello, World' but with your name.")
    time.sleep(1)
    print("2. Introduce yourself with a Biodata.")
    time.sleep(1)
    print("3. A Secret Message.")
    time.sleep(1)
    print("4. Converting (C°) to Far In Height (F°) (It's a pun, please laugh)")
    time.sleep(1)
    print("5. The Operators (Can Also Be Seen In Math!)")
    time.sleep(1)
    print("6. Let's go Mining!")
    time.sleep(1)
    print("7. How Old are you?")
    time.sleep(1)
    print("8. Free Scholarship (Not Legit)")
    time.sleep(1)
    print("9. Wait, I've been here before (Loops)")
    time.sleep(1)
    print("10. Factorials.")
    time.sleep(1)
    print("11. How are pyramids made?")
    time.sleep(1)
    print("12. Shall we check your grade?")
    time.sleep(1)
    print("13. Let's go shopping!")
    time.sleep(1)
    print("14. The Cyber Bank")
    time.sleep(1)
    print("15. Cyber's Favorite Fruits (Lists)")
    time.sleep(1)
    print("16. Modules.")
    time.sleep(1)
    print("17. Custom Functions")
    time.sleep(1)
    print("18. Document Strings.")
    time.sleep(1)
    print("0. Exit")
    
    time.sleep(1)
    print("")
    print("Oh, looks like the creator forgot to change the folder names.")
    choice = int(input("Shall we check them out? (Select a number from the list)\n"))
    if choice == 1:
        os.system('cls')
        time.sleep(1)
        Wait()
        os.system('cls')
        print("Hello, World!")
        time.sleep(5)
        print("A bit simple, isn't it?")
        time.sleep(5)
        print("Let's try adding YOUR name in the text.")
        time.sleep(5)
        print("There is a command in Python where you can ask the user to input their name and it can be inserted in the 'print' output.")
        time.sleep(5)
        print("This was the code: name = input('Please Enter your name: )'")
        time.sleep(5)
        print("And This would be the outcome:")
        time.sleep(1)
        name = input("Please enter a name:  ")
        time.sleep(1)
        print("Oh, Don't forget the 'print' command or else you won't see the output when you run the code")
        tme.sleep(5)
        print("The print could either be ''print(''Hi, '' + name ) or ''print(f''Hi, {name}'')")
        time.sleep(5)
        print(f"Hello, {name}!")
        time.sleep(2)
        print("")
        print("That's a nice name.")
        time.sleep(1)
        print("")
        print("Shall we try the other options?")
        balik()
        continue
    elif choice == 2:
        Wait()
        os.system('cls')
        time.sleep(1)
        print("Say...")
        time.sleep(3)
        print("I don't know you pretty much yet.")
        time.sleep(3)
        print("If you would stay here and explore the other codes, I would love to know about you more.")
        time.sleep(3)
        print("I know!")
        time.sleep(2)
        print("Let's make a Biodata!")
        time.sleep(2)
        print("")
        print("Just fill in the information asked and I'll make one for you")
        time.sleep(2)
        print("Don't worry, your information is safe with me!")
        time.sleep(2)
        print("And the creator is also just a first year, she can't code something that would gather your information and share it online or wherever.")
        time.sleep(5)
        os.system('cls')
        print("Shall we start?")
        time.sleep(3)
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
        print("Hi! I'm " , full_name , "\b.I am a" , gender , "and I am" , age , "years old. My parents are" , Fname , "and" , Mname, "\b. My nationality is " , nationality , "and was born on", birthdate , "at" , birthplace , "and am currently" , civil_status,"\b. My religion is" , religion , "and I am proficient in" , skills , "and not only that but I also like to do" , hobbies , "in my free time. If you have any more questions about me you can contact me through" , email_address , "or" , mobile_no , "\b, and that's all about me. Thank you for reading!")
        time.sleep(1)
        print('')
        ilu = input("That's all I could do.")
        print('')
        print("Nice to meet you, " + full_name ,)
        balik()
        continue
    elif choice == 3:
        Wait()
        time.sleep(2)
        print("Hmmm... you were curious about the secret message, do you?")
        time.sleep(2)
        print("There are passwords for each secret message.")
        time.sleep(2)
        print("Some message gives hints of available passwords.")
        time.sleep(2)
        print("Try this: ''Secret''")
        time.sleep(2)
        print("Just don't tell my creator, how else would you use this program?")
        password = input("Please enter a password: ")
        if password.lower() == "secret":
            os.system('cls')
            print("Access Granted!")
            time.sleep(2)
            print("'Quack!'")
            time.sleep(1)
            print("Acess Granted!")
            print("'Quack!'")
            print(".")
            os.system('cls')
            time.sleep(1)
            print("Acess Granted!")
            print("'Quack!'")
            print("..")
            os.system('cls')
            time.sleep(1)
            print("Acess Granted!")
            print("'Quack!'")
            print("...")
            os.system('cls')
            time.sleep(1)
            print("Acess Granted!")
            print("'Quack!'")
            print("Erm...")
            time.sleep(1)
            print("It's not really a secret, she always say 'Quack', she loves ducks.")
            time.sleep(2)
            print("Try the creator's friends. Here's one, try 'Orte'")
            balik()
            
        elif password.lower() == "orte":
            time.sleep(1)
            print("Access Granted!")
            time.sleep(1)
            print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
            time.sleep(1)
            print("Sadly, it's not n actual load. James added that to his code as a joke.")
            balik()

        elif password.lower() == "azil":
            time.sleep(5)
            print("Boo!")
            time.sleep(2)
            balik()
        else:
            print("Access Denied.")
            print("Hint: First name of the creator.")
            balik()
        print("We better leave before we get caught.")
        time.sleep(2)
        continue
    elif choice == 4:
        Wait()
        print("Is it cold in here?")
        time.sleep(1)
        print("In this program, you could convert Celsius (C°) to Fahrenheit (F°).")

        fahrenheit = eval(input("Please enter temperature in Farenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The conversion of" , fahrenheit , "degrees Fahrenheit is" , round(celsius,2) , "degrees Celcius!")
        time.sleep(2)
        input("Simple, right? ")
        continue
    elif choice == 5:
        x = 5
        Wait()
        print("The Operators!")
        time.sleep(1)
        print("Now Showing In ITCP... and also in Math!")
        time.sleep(3)
        print("It's a simple math, though.")
        time.sleep(3)
        print("The creator practiced the basic math in python in order to program a working calculator.")
        time.sleep(2)
        print("Like no one else has the same idea.")
        time.sleep(2)
        os.system('cls')
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
        print("List of Operations")
        time.sleep(1)
        print(" = Equal or Assign Values")
        time.sleep(1)
        print(" + Addition")
        time.sleep(1)
        print(" - Subtraction")
        time.sleep(1)
        print(" * multiplication")
        time.sleep(1)
        print(" / Division")
        time.sleep(1)
        print(" // Floor Division")
        time.sleep(1)
        print(" % Remainder")
        time.sleep(1)
        print(" ** Exponent")
        time.sleep(2)
        print("Go try it out.")
        time.sleep(1)
        operations()
        print("")
        input("A pretty basic math that you learned in elementary.")
    elif choice == 6:
        os.system('cls')
        Wait()
        print("Welcome to the Digital mines!")
        time.sleep(2)
        print("There's a lot of golds hidden around here, let's try mining some.")
        name = input("Enter your name: ")
        tot = 0
        ans = input("Do you want to mine some gold? (Yes/No):  ")
        print("\n")
        if ans.lower() == "yes": 
            all = tot + 1
            time.sleep(2)
            print(f"Good job, {name}! You have acquired {all} gold!")
            time.sleep(2)
        elif ans.lower() != "no":
            print("Let's find some, ", name )
            time.sleep(2)
        else:
            print("Erm...")
            time.sleep(2)
        pass
    elif choice == 7:
        Wait()
        print("Now how old are you?")
        time.sleep(3)
        print("Are you even old enough to use this program?")
        time.sleep(2)
        print("Just kidding, there is no age limit in this program.")
        time.sleep(2)
        print("It can be used for all ages.")
        time.sleep(2)
        age = eval(input("But really, how old are you? "))
        if age >= 1 and age <= 7:
            print("A child.")
            time.sleep(2)
            print("I see that you're starting to learn code in such a young age.")
            input("Go back (Y/N)? ")
        elif age >= 8 and age<= 13:
            print("Hmm... Preteen")
            time.sleep(2)
            print("Did you find programming cool? Do you want to impress your friends into making them think that you're hacking but really what you did was only 'print(''Hello, World'').")
            time.sleep(2)
            input("Go back (Y/N)? ")
        elif age >= 14 and age<= 18:
            print("Ah, a teenager.")
            time.sleep(2)
            print("Are you preparing for college, perhaps?")
            input("Go back (Y/N)? ")
        elif age >= 19 and age<= 31:
            print("You're an early adult")
            time.sleep(2)
            print("I bet you're often getting the message 'Mag-asawa ka na'")
            input("Go back (Y/N)? ")
        elif age >= 32 and age<= 59:
            print("You're a mid adult")
            time.sleep(2)
            print("Indeed, mag-asawa ka na.")
            input("Go back (Y/N)? ")
        elif age >= 60 and age <= 100:
            print("You're a senior")
            time.sleep(2)
            print("People would start respecting you more at this point, even treat you like you can't do things anymore.")
            time.sleep(2)
            print("In bitter reality, it's true, isn't it?")
            time.sleep(2)
            print("You can't do the things you used to do when you were younger.")
            time.sleep(2)
            print("How you wish you could be young again...")
            time.sleep(2)
            print("When things used to be fun.")
            time.sleep(2)
            print("When time is always free in your hands.")
            input("Go back (Y/N)?")
        else:
            print("Erm... were you born during the caveman era?")
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
                    print("Welcome, Freshman!")
                elif isSY.lower() == "s":
                    print("Welcome back, Sophomore!")
                elif isSY.lower() == "j":
                    print("You're almost there, Junior!")
                elif isSY.lower() == "r":
                    print("A few steps left, Senior!")
                else:
                    print("Invalid year level, please try again")
                isScho = input("Do you need this scholarship?(Y/N): ")
                if isScho.lower() == "y":
                    print("You have been granted a full scholarship, thank you for choosing DLL")
                    balik()
                else:
                    print("Very well.")
                    time.sleep(3)
                    print("Someone's rich and doesn't need scholarship.")
                    balik()
            else:
                print("Sorry, you are not eligible")
                balik()
        else:
            print("Sorry, you are not eligible")
            balik()
    elif choice == 9:
        Wait()
        print("It feels like Deja Vu.")
        time.sleep(1)
        print("It's the Loops!")
        time.sleep(1)
        print("Well, you can tell the purpose of the code based on it's name.")
        time.sleep(1)
        print("You can repeat a code block as many times you want by using Loops."))
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
        print("'Hello, World', Indeed")
        balik()
    elif choice == 10:
        Wait()
        print("Welcome to Factorials.")
        factorial = 1
        print("")
        start = eval(input("Enter the number you want to factorial: "))
        for x in range(start,0,-1):
            print(x)
            factorial *= x
        print(f"the factorial of {start} is {factorial} ")
        time.sleep(1)
        print("As simple as that.")
        balik()
    elif choice == 11:
        Wait()
        print("How are Pyramids made?")
        time.sleep(1)
        print("... in Python.")
        time.sleep(1)
        print("I was informed that the creator used a lot of 'print' commands in her FirstEverProgram.")
        time.sleep(1)
        print("And she was only making a diamond.")
        time.sleep(1)
        print("And just recently, she learned how to make shapes with loops.")
        time.sleep(1)
        print("It's more easier and less of a hussle.")
        time.sleep(2)
        print("Let's try to make a simple triangle.")
        time.sleep(2)
        print("That apparently looks like a slide.")
        time.sleep(1)
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
        os.system('cls')
        

                    
    elif choice == 12:
        Wait()
        grades()
    elif choice == 13:
            Wait()
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
        Wait()
        main()
    elif choice == 15:
        Wait()
        learn_lists()
    elif choice == 16:
        Wait()
        learn_modules()
    elif choice == 17:
        Wait()
        learn_functions()
    elif choice == 18:
        Wait()
        learn_docstrings()
    elif choice == 0:
        os.system('cls')
        time.sleep(5)
        print("Whew, that's a lot... was it?")
        time.sleep(5)
        print("Somehow... I don't remember what we'vre been through.")
        time.sleep(5)
        print("My memories were programmed to instantly reset as soon as you chose '0'.")
        time.sleep(5)
        print("Well... if you checked everything in the menu or not, I thank you for using me.")
        time.sleep(5)
        print("I'll completely restart back to normal after saying this farewell.")
        time.sleep(5)
        print("The program will be terminated.")
        time.sleep(5)
        print("And when you come back, I won't remember you.")
        time.sleep(5)
        print("We'll have to make a new set of memories again.")
        time.sleep(5)
        print("...")
        print("")
        time.sleep(10)
        print("Farewell.")
        time.sleep(3)
        break
