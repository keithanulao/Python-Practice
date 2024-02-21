import random

# The correct password
correct_password = random.randint(0, 9999)

# Monte Carlo simulation
attempts = 0
while True:
    guess = random.randint(0, 9999)
    attempts += 1
    if guess == correct_password:
        print(f"Correct password found: {guess}")
        print(f"Total attempts: {attempts}")
        break
