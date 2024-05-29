#Cows and Bulls Puzzle Solver

import random
import os


def generate_possible_numbers():
  """Generates a list of all possible 4-digit numbers with unique digits."""
  possible_numbers = []
  for i in range(1000, 10000):
    if len(set(str(i))) == 4:
      possible_numbers.append(str(i))
  return possible_numbers

def get_cow_bull_count(secret_number, guess):
  """Calculates the number of cows and bulls for a given guess."""
  cows = 0
  bulls = 0
  for i in range(4):
    if secret_number[i] == guess[i]:
      cows += 1  # Correct number in the correct position (cow)
    elif guess[i] in secret_number:
      bulls += 1  # Correct number in the wrong position (bull)
  return cows, bulls

def filter_possible_numbers(possible_numbers, guess, cows, bulls):
  """Filters the list of possible numbers based on cow/bull feedback."""
  new_possible_numbers = []
  for number in possible_numbers:
    new_cows, new_bulls = get_cow_bull_count(number, guess)
    if new_cows == cows and new_bulls == bulls:
      new_possible_numbers.append(number)
  return new_possible_numbers

def solve_cows_and_bulls():
  """Main solver loop for cows and bulls."""
  possible_numbers = generate_possible_numbers()
  guesses = 0

  while len(possible_numbers) > 0:
    # Make a guess (can be optimized with strategies)
    guess = random.choice(possible_numbers)
    guesses += 1
    print(f"\nGuess #{guesses}: {guess}")

    cows, bulls = int(input("Enter cows: ")), int(input("Enter bulls: "))

    # Filter possible numbers based on feedback
    possible_numbers = filter_possible_numbers(possible_numbers, guess, cows, bulls)

  # Solved the puzzle
  print(f"\nThe secret number is: {possible_numbers[0]} (in {guesses} tries)")

if __name__ == "__main__":
  os.system("cls")
  solve_cows_and_bulls()
