#C# translation 2.1

import time
import os

yellow = "\033[93m"
reset = "\033[0m"

def greet():
    os.system("cls")
    username = input("What is your name? ")
    print()
    time.sleep(0.5)
    user_age = input("What is your age? ")
    print()
    time.sleep(0.5)
    pet_type = input("What type of pet do you have? ")
    print()
    time.sleep(0.5)
    pet_name = input("What is the name of your pet? ")
    print()
    time.sleep(0.5)
    pet_color = input("What color is your pet? ")
    print()
    time.sleep(0.5)
    ownership_year = input("How many years have you owned your pet? ")

    print()
    time.sleep(2)
    print(f"{yellow}{username}{reset}", " is ", f"{yellow}{user_age}{reset}", " years old")
    time.sleep(2)
    print(f"{yellow}{username}{reset}", " has a ", f"{yellow}{pet_color}{reset}", f"{yellow}{pet_type}{reset}", " named ", f"{yellow}{pet_name}{reset}", )
    time.sleep(2)
    print(f"{yellow}{username}{reset}", " has owned ", f"{yellow}{pet_name}{reset}", " for ", f"{yellow}{ownership_year}{reset}", " years")
    time.sleep(2)
    print()

def restart():
    while True:
        restart = input("Type " f"{yellow}(RESTART){reset}" " to restart the program: ").lower().replace(' ','')
        if restart == "restart":
            print("***Restarting Program***")
            time.sleep(1)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("**Invalid Input**")
            print()
            print("Try Again")
            time.sleep(2)
            print()
            os.system("cls")

def main():
    while True:
        greet()
        restart()

if __name__ == "__main__":
    main()