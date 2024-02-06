import re

def remove_spaces_and_punctuation(text):
    # Remove spaces
    text = text.replace(" ", "")
    
    # Remove punctuation using regular expressions
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

def count_characters(cleaned_input):
    return len(cleaned_input)

def is_palindrome(s):
    return s == s[::-1]

#####################################################################

while True:
    user_input = input("Insert a phrase (or 'exit' to exit): ")
    if user_input.lower() == 'exit':
        break

    cleaned_input = remove_spaces_and_punctuation(user_input)
    print("Cleaned input:", cleaned_input)
    print()
    print("Number of characters: ", count_characters(cleaned_input))
    print(is_palindrome(cleaned_input), ", This is not a Palindrome")
    print()
    print("Try a new phrase.")

print("Exiting the program.")