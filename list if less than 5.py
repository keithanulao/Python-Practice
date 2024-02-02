a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)

user_number = int(input("choose any whole number:"))
less_than_number = []


for number in a:
    if number < user_number:
        less_than_number.append(number)

print(less_than_number)