import pandas as pd
import os

# Assign grades based on marks
def assign_grade(marks):
    if 0 <= marks <= 9:
        return 'F'
    elif 10 <= marks <= 19:
        return 'F'
    elif 20 <= marks <= 29:
        return 'F'
    elif 30 <= marks <= 39:
        return 'F'
    elif 40 <= marks <= 49:
        return 'F'
    elif 50 <= marks <= 59:
        return 'D'
    elif 60 <= marks <= 69:
        return 'C'
    elif 70 <= marks <= 79:
        return 'B'
    elif 80 <= marks <= 89:
        return 'A'
    elif 90 <= marks <= 100:
        return 'A'
    else:
        return 'Invalid'

def file_search(file_path):
    while True:
        try:
            return pd.read_csv(file_path, header=0)
        except FileNotFoundError:
            print("\nFile not found, ensure the file path is correct...")
            new_path = input("\nPlease enter the correct file path: ")
            file_path = new_path

def compute_grade(file_path):
    """Computes and prints the graded DataFrame."""
    try:
        data_frame = file_search(file_path)

        # Sort DataFrame by 'Marks' in descending order
        sorted_df = data_frame.sort_values(by='Marks', ascending=False)

        # Apply grading function to the sorted DataFrame
        sorted_df['Grade'] = sorted_df['Marks'].apply(assign_grade)

        # Select desired columns
        selected_df = sorted_df[['Name', 'Marks', 'Grade']]

        # Replace names with "Null" for marks less than 70
        selected_df.loc[selected_df['Marks'] < 70, 'Name'] = 'Null'

        # Remove rows with 'NaN' or 'Invalid' values
        cleaned_df = selected_df.dropna()
        cleaned_df = cleaned_df[cleaned_df['Grade'] != 'Invalid']

        # Print the DataFrame
        print("\n", cleaned_df.to_string(index=False))
        print('-' * 20, "\n")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    os.system("cls")
    file_path = "C:\\Users\\keith\\OneDrive\\Desktop\\Sheet21.csv"
    compute_grade(file_path)

#hi my name is keith