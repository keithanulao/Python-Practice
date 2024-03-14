from datetime import date
import time
import random

yellow = "\033[93m"
reset = "\033[0m"

def age_calc():
    print()
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

while True:
    start = input("Would you like to try and calculate your age? (yes/no): ").lower().replace(' ','')
    if start == "no":
        break  

    elif start == "yes":
        age_calc()
        print()

    else:
        print("Please enter a valid input (yes/no)")
        print()

    