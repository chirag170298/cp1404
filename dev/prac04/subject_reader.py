"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def display_data(data):
    for subject in data:
        code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[2]
        print(f"{code:7} is taught by {lecturer:12}  and has  {number_of_students:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    parts = []
    input_file = open(FILENAME)
    for line in input_file:
        part = line.strip().split(',')
        part[2] = int(part[2])
        parts.append((part))
    input_file.close()
    return (parts)

    # print(line)  # See what a line looks like
    # print(repr(line))  # See what a line really looks like
    # line = line.strip()  # Remove the \n
    # parts = line.split(',')  # Separate the data into its parts
    # print(parts)  # See what the parts look like (notice the integer is a string)
    # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    # print(parts)  # See if that worked
    # print("----------")


main()
