while True:
    user_number = int(input("Choose any whole number (or 0 to exit): "))
    if user_number == 0:
        break

    list_range = list(range(1, user_number + 1))

    divisor_list = []

    for number in list_range:
        if user_number % number == 0:
            divisor_list.append(number)

    print("Divisors of", user_number, ":", divisor_list)
    print()
    print("Try a new number")

print("Exiting the program.")