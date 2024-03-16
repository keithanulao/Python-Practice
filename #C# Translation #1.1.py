#C# Translation #1.1
import os 
import time

yellow = "\033[93m"
reset = "\033[0m"

#Greeting
os.system("cls")
name = (input("what is your name? "))
print()
print("Hello " + f"{yellow}{name}{reset}" " :) ")
print()

time.sleep(1.5)
os.system("cls")

def cont():
    while True:
        choice = input("Input " f"{yellow}(Spacebar){reset}" " to continue ").replace(' ','')
        if choice == '':
            os.system("cls")
            break
        else:
            os.system("cls")
            print("***Invalid Input***")
            print()

def add():
    while True:
        try:
            input1 = int(input("Choose the first number you would like to add: "))
            print("First Integer: " f"{yellow}{input1}{reset}")
            print()
            input2 = int(input("Choose the second number you would like to add: "))
            print("First Integer: " f"{yellow}{input2}{reset}")
            print()
            sum = input1 + input2 
            print("The " f"{yellow}sum{reset}" " of the values is: " f"{yellow}{sum}{reset}")
            print()

            cont() 
            break
        except ValueError:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}Integers Only{reset}" ", Try Again")
            print()

def subtract():
    while True:
        try:
            input1 = int(input("Choose the first number you would like to subtract: "))
            print("First Integer: " f"{yellow}{input1}{reset}")
            print()
            input2 = int(input("Choose the second number you would like to subtract: "))
            print("First Integer: " f"{yellow}{input2}{reset}")
            print()
            difference = input1 - input2 
            print("The " f"{yellow}difference{reset}" " of the values is: " f"{yellow}{difference}{reset}")
            print()

            cont() 
            break
        except ValueError:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}Integers Only{reset}" ", Try Again")
            print()

def multiply():
    while True:
        try:
            input1 = int(input("Choose the first number you would like to multiply: "))
            print("First Integer: " f"{yellow}{input1}{reset}")
            print()
            input2 = int(input("Choose the second number you would like to multiply: "))
            print("First Integer: " f"{yellow}{input2}{reset}")
            print()
            product = input1 * input2 
            print("The " f"{yellow}product{reset}" " of the values is: " f"{yellow}{product}{reset}")
            print()

            cont() 
            break
        except ValueError:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}Integers Only{reset}" ", Try Again")
            print()

def divide():
    while True:
        try:
            input1 = int(input("Choose the first number you would like to divide: "))
            print("First Integer: " f"{yellow}{input1}{reset}")
            print()
            input2 = int(input("Choose the second number you would like to divide: "))
            print("First Integer: " f"{yellow}{input2}{reset}")
            print()
            quotient = input1 // input2 
            modulo = input1 % input2
            print("The " f"{yellow}quotient{reset}" " of the values is: " f"{yellow}{quotient}{reset}")
            print("And the " f"{yellow}remainder{reset}" " is: " f"{yellow}{modulo}{reset}") 
            print()

            cont() 
            break
        except ValueError:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}Integers Only{reset}" ", Try Again")
            print()
        except ZeroDivisionError:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}Dividing by Zero{reset}" ", Try Again")
            print()

def choice():
    while True:
        option = input("Would you like to: " f"{yellow}(add/subtract/multiply/divide){reset}" " or type " f"{yellow}(EXIT){reset}" " to exit the program ").lower().replace(' ','')
        print()
        if option == "exit":
            print("***Exiting Program in 5 seconds***")
            print()
            print("Goodbye " f"{yellow}{name}{reset}" " :)")
            print()
            time.sleep(5)
            os.system("cls")
            break
        elif option == "add":
            add()
        elif option == "subtract":
            subtract()
        elif option == "multiply":
            multiply()
        elif option == "divide":
            divide()
        else:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}(add/subtract/multiply/divide){reset}" ", Try Again")
            print()

def restart():
    while True:
        restart = input("Type " f"{yellow}(RESTART){reset}" " to start the program: ").lower().replace(' ','')
        if restart == "restart":
            print("***Restarting Program***")
            time.sleep(1.5)
            os.system("cls")
            choice()
        else:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print(f"{yellow}(RESTART){reset}" ", Try Again")
            print()

choice()
restart()
