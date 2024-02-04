user_number = int(input("chose any whole number: "))

list_range = list(range(1, user_number +1))

divisor_list = []

for number in list_range:
    if user_number % number == 0:
        divisor_list.append(number)

print(divisor_list)
print( )
print("Try a new number")