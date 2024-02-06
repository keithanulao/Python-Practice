import re

def remove_spaces_and_punctuation(text):
    # Remove spaces
    text = text.replace(" ", "")
    
    # Remove punctuation using regular expressions
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

while True:
    user_input = input("Insert a phrase (or 'exit' to exit): ")
    if user_input.lower() == 'exit':
        
        break

    cleaned_input = remove_spaces_and_punctuation(user_input)
    print("Cleaned input:", cleaned_input)
    print(" ")
    print("Try a new phrase.")


print("Exiting the program.")