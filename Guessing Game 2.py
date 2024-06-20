#Guessing Game 2 

import random
import os
os.system("cls")

def guess_number():
  """Prompts user for min and max number, guesses a number between them based on feedback."""

  print("Think of a number between a certain range. I will try to guess it!")

  # Get user input for min and max number
  min_number = int(input("Enter the minimum number: "))
  max_number = int(input("Enter the maximum number: "))
  print(f"Think of a number between {min_number} and {max_number}. I will try to guess it!")

  guess = random.randint(min_number, max_number)
  num_guesses = 0  # Initialize guess counter

  while True:
    num_guesses += 1  # Increment guess counter before prompting

    user_response = input(f"Is your number {guess}? (higher/lower/correct): ").lower()

    if user_response == "correct":
      print(f"I guessed your number in {num_guesses} tries!")
      break
    elif user_response == "higher":
      min_number = guess + 1
    elif user_response == "lower":
      max_number = guess - 1
    else:
      print("Invalid input. Please enter 'higher', 'lower', or 'correct'.")

    # Update guess based on feedback
    guess = random.randint(min_number, max_number)

if __name__ == "__main__":
  guess_number()
