#Document "Control-F"

import os

def search_document(document_path, search_terms):
  """
  This function searches a document at the specified path for user-provided search terms 
  and prints the terms with their counts.

  Args:
      document_path: The path to the document file (including filename).
      search_terms: A list of strings representing the words or phrases to search for.
  """

  # Check if file exists
  if not os.path.isfile(document_path):
    print(f"Error: File not found at {document_path}")
    return

  # Read document text
  try:
    with open(document_path, 'r') as document_file:
      document_text = document_file.read()
  except OSError as error:
    print(f"Error reading document: {error}")
    return

  # Split the document text into lowercase words, removing punctuation.
  words = [word.strip().lower() for word in document_text.split() if word.isalpha()]

  # Create a dictionary to store word counts
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  # Search for user-provided terms
  for term in search_terms:
    term_count = word_counts.get(term.lower(), 0)  # Get count, default 0 if not found
    if term_count > 0:
      print(f"\n{term}: {term_count} occurrences\n")
  
  # If no search terms were found
  if not any(term_count > 0 for term_count in word_counts.values()):
    print("No search terms found in the document.")

os.system("cls")

# Get document path (replace with actual path)
document_path = "C:\\Users\\New PC\\Desktop\\Test Folder\\test.txt"  # Replace with your filename

# Get user input for search terms (replace with your preferred input method)
search_terms = input("Enter words or phrases separated by commas (e.g., apple, banana, example): ").split(",")
search_terms = [term.strip() for term in search_terms]  # Remove extra spaces

# Call the search function
search_document(document_path, search_terms)
