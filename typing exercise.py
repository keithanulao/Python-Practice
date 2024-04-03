#Typing Exercise

import os 
import time
import random
yellow = "\033[93m"
reset = "\033[0m"

def exercise():
    """Scrambles a user-provided phrase, times typing speed, and displays errors."""

    os.system("cls")  # Clear screen on Windows (adjust for other OS)

    phrase = input("Type a phrase to be randomly scrambled: ").split()
    scrambled_phrase = random.sample(phrase, len(phrase))
    joined_scrambled = " ".join(scrambled_phrase)

    print("\nHere is the scrambled phrase:")
    print(joined_scrambled)

    print("\nGet ready to type the whole phrase...")
    time.sleep(2)

    start_time = time.time()  # Start time for timer
    user_input = input("\nBegin Typing: ").lower().split()  # Convert input to lowercase and split into words

    end_time = time.time()  # End time for timer
    total_time = round(end_time - start_time, 2)  # Calculate typing time

    correct_words = 0
    errors = []
    # Compare user input with scrambled phrase
    for i, word in enumerate(scrambled_phrase):
        if user_input[i].lower() == word.lower():  # Case-insensitive comparison
            correct_words += 1
        else:
            errors.append(f"Incorrect: '{user_input[i]}' (should be '{word}')")

    total_words = len(scrambled_phrase)  # Calculate total words in the scrambled phrase
    words_per_minute = round((correct_words / total_time) * 60, 2)  # Calculate WPM

    accuracy = round((correct_words / total_words) * 100, 2)  # Calculate accuracy based on scrambled phrase

    print("\n**Results**")
    print(f"Typing Time: {total_time} seconds")
    print(f"Words Per Minute: {words_per_minute}")
    print(f"Accuracy: {accuracy}% ({correct_words} correct words out of {total_words})")

    if errors:
        print("\n**Errors**:")
        for error in errors:
            print(error)
    else:
        print("\nCongratulations! No errors detected!")

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
        exercise()
        restart()

if __name__ == "__main__":
    main()
