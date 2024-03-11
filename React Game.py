import random
import time

def get_user_input(message):
    """Gets user input from the terminal."""
    while True:
        user_input = input(message)
        if user_input.lower() == "react":
            return True
        else:
            print("Invalid input. Please type 'react' to proceed.")

def main():
    print("Welcome to the Reaction Time Test!")
    print("Get ready to react as quickly as possible!")

    # Generate random delay between 3.0 and 6.0 seconds
    delay = round(random.uniform(3.0, 6.0), 1)
    print(f"The prompt will appear in {delay} seconds. Don't start reacting yet!")

    # Simulate a prompt appearing (replace with actual prompt if needed)
    time.sleep(delay)  # Wait for the random delay
    start_time = time.time()  # Record start time after the delay

    print()
    print()
    print("** REACT! **")
    print()
    print()

    if get_user_input("Press 'react' to record your time: "):
        reaction_time = time.time() - start_time
        print(f"Your reaction time: {reaction_time:.2f} seconds")
    else:
        print("Invalid input. Test aborted.")

while True:
    print()
    print()
    start = input("Would you like to play? (yes) or (no): ")
    print()
    print()
    if start == "yes":
        main()
    elif start == "no":
        print("Good Game :) ")
        break
    else:
        print("Invalid Input, Respond with (yes) or (no): ")