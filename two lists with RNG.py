import random

a = random.sample(range(1, 20), 10)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(a) & set(b))

print("Random list A:", a)
print("List B:", b)
print("Common elements:", common_elements)