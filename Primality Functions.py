import os
import time

def prime_calculator():
    os.system("cls")  
    try:
        num = int(input("Give me a number: "))
        if num > 1:
            is_prime = True
            for i in range(2, (num // 2) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, "is a prime number")
            else:
                print(num, "is not a prime number")
        else:
            print(num, "is not a prime number")  
    except ValueError:
        print("ERROR... Invalid input. Please enter a number.")
        time.sleep(1)

def main():
    while True:
        print()
        cont = input("Would you like to continue? (SPACEBAR to continue, Exit to exit) ").lower().replace(' ', '')
        if cont == '':
            print()
            print("(Re)Starting...")
            time.sleep(1)
            prime_calculator()
        elif cont == "exit":
            print()
            print("Exiting...")
            time.sleep(1)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("***ERROR***")
            print()
            print("Enter a valid input (SPACEBAR or 'exit')")

if __name__ == "__main__":
    main()
