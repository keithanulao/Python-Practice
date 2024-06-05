#File Overlap Reader

def compare_and_print_matches(filename1, filename2):
  """
  This function reads two text files containing number lists, compares them, 
  and prints the matching numbers.

  Args:
      filename1: The path to the first text file (including filename).
      filename2: The path to the second text file (including filename).
  """
  # Read the contents of both files into sets for efficient lookups
  try:
    with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
      list1 = set(line.strip() for line in file1)
      list2 = set(line.strip() for line in file2)
  except FileNotFoundError:
    print(f"Error: One or both files {filename1} and {filename2} not found.")
    return

  # Find the intersection of the sets (matching numbers)
  matches = list1.intersection(list2)

  # Print the matching numbers
  if matches:
    print("Matching numbers:")
    for number in matches:
      print(number)
  else:
    print("No matching numbers found between the two lists.")

# Specify the filenames (replace with your actual filenames)
filename1 = "C:\\Users\\New PC\\Desktop\\list_1.txt"
filename2 = "C:\\Users\\New PC\\Desktop\\list_2.txt"


compare_and_print_matches(filename1, filename2)
