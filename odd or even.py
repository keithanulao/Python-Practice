number = int(input("Chose any whole number: "))
new_number = number / 2

div_by_4 = number / 4

if div_by_4.is_integer():
    print("This number is dvisible by 4")
else:
    if new_number.is_integer():
        print("This number is an even number.")
    else:
        print("This number is an odd number.")
