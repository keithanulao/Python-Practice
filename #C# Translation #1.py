#C# Translation #1
import os 

yellow = "\033[93m"
reset = "\033[0m"

#Greeting
print()
name = (input("what is your name? "))
print("Hello: " + f"{name}")

def get_user_choice():
  """Gets user input for addition or division and validates it."""
  while True:
    print()
    choice = input("Would you like to add or divide? ").lower().replace(' ', '')
    print()
    if choice in ("add", "divide"):
      return choice
    else:
      print("Please enter a valid input: (add/divide)")

def restart():
  """Prompts user to restart and validates input."""
  while True:
    restart_choice = input("Would you like to choose again? (yes/no) ").lower().replace(' ', '')
    if restart_choice in ("yes", "no"):
      if restart_choice == "yes":
        print("Restarting...")
        return True  # Return True to signal restart
      else:
        print("Exiting Program")
        print()
        break  # Exit the entire loop (program termination)
    else:
      print("Please enter a valid input: (yes/no)")
      print()

def add():
  """Adds two numbers entered by the user."""
  try:
    num1 = int(input("Enter your first number to be added: "))
    num2 = int(input("Enter your second number to be added: "))
    total = num1 + num2
    print()
    print(f"The sum of {yellow}{num1}{reset} and {yellow}{num2}{reset} is: {yellow}{total}{reset}")
    print()
  except ValueError:
    print("Invalid input. Please enter only numbers.")
    print()

def divide():
  """Divides two numbers entered by the user."""
  try:
    num1 = int(input("Enter your first number to be divided: "))
    num2 = int(input("Enter your second number to divide by: "))
    if num2 == 0:
      print("Error: Cannot divide by zero. Please enter a non-zero number.")
    else:
      result = num1 / num2
      result_rounded = round(result, 2)
      print()
      print(f"{yellow}{num1}{reset} divided by {yellow}{num2}{reset} is: {yellow}{result_rounded}{reset}")
      print()
  except ValueError:
    print("Invalid input. Please enter only numbers.")

# Main loop (modified)
user_wants_to_continue = True
while user_wants_to_continue:
  choice = get_user_choice()
  if choice == "add":
    add()
  elif choice == "divide":
    divide()
  user_wants_to_continue = restart()  # Call restart and store return value

  # Check the return value from restart and clear screen if True
  if user_wants_to_continue:
    # Clear the screen using os module (optional)
    os.system('cls' if os.name == 'nt' else 'clear')  # Platform-specific clear

