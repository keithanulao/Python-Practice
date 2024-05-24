#Element Searcher 
import os
import time
import random 


def restart():
    while True:
        restart = input("\nPress (ENTER) to restart the program ").lower().replace(' ','')
        if restart == "":
            print("\n***Restarting Program***")
            time.sleep(1)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("**Invalid Input**")
            print("\nTry Again")
            time.sleep(2)
            os.system("cls")


def is_number_in_ordered_list(ordered_list, number):
  """Checks if a number exists within a sorted (ascending) list."""
  for item in ordered_list:
    if item == number:
      return True  # Number found in the list, return True
    elif item > number:
      return False  # Number is smaller than current item, cannot exist in a sorted list
  return False  # Reached the end of the list without finding the number


def main():
    while True:
        while True:
            try:
                os.system("cls")
                number_to_check = int(input("Type in a desired number to check to see if it is on the list: "))
                break
            except ValueError:
                print("\n***ERROR***" "\nInput an Integer")
                time.sleep(1)
                os.system("cls")

        ordered_list = [1, 3, 5, 7, 9]

        if is_number_in_ordered_list(ordered_list, number_to_check):
            print(f"\n{number_to_check} is in the list.")
        else:
            print(f"\n{number_to_check} is not in the list.")

        restart()

if __name__ == "__main__":
   main()