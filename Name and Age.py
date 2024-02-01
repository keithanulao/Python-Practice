from datetime import date


name = input("What is your name?")
print("You name is " + name )

age = int(input("How old are you?"))
print("You are " + str(age) + " years old")

today = date.today()
print("Today's date is")
print(today)

years_to_come = 100 - age 
predicted_year = years_to_come + today.year
print("And you will turn 100 at the year of " + str(predicted_year))