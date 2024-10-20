"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list =[]
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list.append([parts[0], parts[1], parts[2]])
    return data_list
    input_file.close()

def display_subject_data(data):
    for item in data:
        print(f"{item[0]} is taught by {item[1]} and has {item[2]} students")


main()