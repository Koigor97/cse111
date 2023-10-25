import csv

I_NUMBER_INDEX = 0


def main():
    student_ID = input("Please enter your student ID number: ")
    student_name = read_dict("students.csv", I_NUMBER_INDEX)
    if "-" in student_ID:
        is_student_valid = student_ID.replace("-", "")
        if is_student_valid in student_name:
            result = student_name[is_student_valid]
            print(result)
        else:
            return "No such student"
    elif len(student_ID) < 9:
        print("Invalid I-Number: too few digits")
    elif len(student_ID) > 9:
        print("Invalid I-Number: too many digits")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename) as csv_file:
        data = csv.reader(csv_file)
        next(data)
        student_dict = {}
        for rows in data:
            key = rows[key_column_index]
            student_dict[key] = str(rows[1])
        return student_dict


if __name__ == "__main__":
    main()
