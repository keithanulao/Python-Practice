from datetime import date
import time
import random
import os

yellow = "\033[93m"
reset = "\033[0m"

def age_calc():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    print()

    print(f"{yellow}{name}{reset} is {yellow}{age}{reset} years old")
    print()
    print("Fetching today's date...")
    print()

    delay = round(random.uniform(2.0, 3.0),3)
    time.sleep(delay)  
   
    today = date.today()
    print("Today's date is")
    print(f"{yellow}{today}{reset}")
    print()

    years_to_come = 100 - age
    predicted_year = years_to_come + today.year
    print("And you will turn 100 at the year of " + f"{yellow}{predicted_year}{reset}")
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
            os.system("cls")
            print("**Enter a valid input** " f"{yellow}(Spacebar){reset} " )
            print()

while True:
    start = input("Would you like to try and calculate your age? " f"{yellow}(yes/no){reset}"": " ).lower().replace(' ','')
    os.system("cls")
    if start == "no":
        print("***Ending Program***")
        break  

    elif start == "yes":
        age_calc()
        print()
        cont()

    else:
        os.system("cls")
        print("***Please enter a valid input*** " f"{yellow}(yes/no){reset}")
        print()

    