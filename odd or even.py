import os

yellow = "\033[93m"
reset = "\033[0m"

def odd_or_even():
    new_number = number / 2
    div_by_4 = number / 4

    if div_by_4.is_integer():
        print(f"{yellow}{number}{reset}" " is dvisible by " f"{yellow}4{reset}")
    else:
        if new_number.is_integer():
            print(f"{yellow}{number}{reset}" " is an " f"{yellow}even number{reset}")
        else:
            print(f"{yellow}{number}{reset}" " is an " f"{yellow}even number{reset}")
        print()
        print()

def cont():
    while True:
        prompt2 = input("Press " f"{yellow}(Spacebar){reset}" " to Continue: ").replace(' ','')
        print()
        if prompt2 == "":
            os.system("cls")
            break
        else:
            print()
            print("**Enter a valid input** " f"{yellow}(Spacebar){reset} " )
            print()
    
while True:
    print()
    prompt1 = input("Would you like to start? " f"{yellow}(yes/no){reset} " )
    print()

    if prompt1 == "yes":
        try:
            os.system("cls")
            number = int(input("Chose any whole number: "))
            odd_or_even()
            cont()
        except ZeroDivisionError:
            print("Cannot divide by zero, try again")
    elif prompt1 == "no":
        print("**Ending Program**")
        break
    else:
        os.system("cls")
        print("**Enter a valid input**")
        



