import random


while True:
    player = str(input("Would you like to play? ")).replace(' ', '').lower()
    
    if player == "no":
        print("Good Game :D")
        break
    
    elif player == "yes":
       
        lower = int(input("Set the lower limit: "))
        upper = int(input("Set the upper limit: "))
        rand_numb = random.randint(lower, upper)

        # Counter
        amount = 0

        while True:
            guess = int(input(f"Guess the number between {lower} and {upper}: "))
            amount += 1
            if guess == rand_numb:
                print(f"Congratulations! You guessed the number in {amount} tries.")
                print()
                break
            elif guess < rand_numb:
                print("Too low. Try again.")
                print()
            else:
                print("Too high. Try again.")
                print()

    else:
        print("Invalid input. Please enter yes or no")
    