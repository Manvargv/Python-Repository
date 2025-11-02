def main():
    # Create an empty dictionary to store student information
    student_info = {}

    # Adding a student to the dictionary
    name = "Alice Johnson"
    student_info[name] = {
        "ID": "S001",
        "GPA": 3.7,
        "Credits Completed": 45,
        "Grades": ["A", "B+", "A-"]
    }

    # Add another student
    name2 = "Brian Smith"
    student_info[name2] = {
        "ID": "S002",
        "GPA": 3.2,
        "Credits Completed": 60,
        "Grades": ["B", "B-", "C+"]
    }

    # Print the full dictionary
    print("\nFull Student Information Dictionary:")
    print(student_info)

    # Print a heading for listing student names
    print("\n--- Student Names ---")
    for name in student_info:
        print(name)

    # Print a heading for accessing student information
    print("\n--- Accessing Student Information ---")
    print("Name\t\t\tID\tGPA\tCredits\tGrades")

    for name, info in student_info.items():
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits Completed']}\t{info['Grades']}")

    # Removing a student
    print("\n--- Removing a Student ---")
    removed_student = student_info.pop("Brian Smith")
    print(f"Removed: Brian Smith")
    print("\nUpdated Student Information Dictionary:")
    print(student_info)

    # Accessing GPA information
    print("\n--- Accessing GPA Information ---")
    for name in student_info:
        gpa = student_info.get(name).get("GPA")
        print(f"{name}'s GPA: {gpa}")

    # Clearing all student information
    print("\n--- Clearing Student Registry ---")
    student_info.clear()
    print("Cleared Dictionary:", student_info)

    # Final statement
    print("\nCompleted by, Manuel Vargas")


# Call the main function
if __name__ == "__main__":
    main()
