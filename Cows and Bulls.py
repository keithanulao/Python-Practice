#Cows and Bulls
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

def generate_secret_number():
    os.system("cls")
    """Generates a random 4-digit number with no duplicate digits."""
    while True:
        secret_number = str(random.randint(1000, 9999))  # Generate random 4-digit number
        if len(set(secret_number)) == 4:  # Check for unique digits
            return secret_number

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

def play_cows_and_bulls():
    """Main game loop for cows and bulls."""
    secret_number = generate_secret_number()
    guesses = 0
    print("Guess the 4-digit number (no leading zeros)!")

    while True:
        guess = input("\nEnter your guess: ")
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid guess. Please enter a 4-digit number.")
            continue
        guesses += 1

        cows, bulls = get_cow_bull_count(secret_number, guess)

        print(f"Cows: {cows}, Bulls: {bulls}")

        if cows == 4:
            print(f"\nCongratulations! You guessed the number in {guesses} tries.")
            break

def main(): 
    while True:
        play_cows_and_bulls()
        restart()

if __name__ == "__main__":
    main()
