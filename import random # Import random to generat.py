import random  # Import random to generate random employee ID numbers


# Function to create a new employee
def create_employee(employee_list, existing_ids, existing_names):
    # Ask the user for the employee's name
    while True:
        name = input("Enter the employee's name: ").strip()

        # Check if the name already exists (ignore case sensitivity)
        if name.lower() in [n.lower() for n in existing_names]:
            print("This employee already exists. Please enter a different name.")
        else:
            break

    # Add the name to the existing names list
    existing_names.append(name)

    # Generate a random number between 1 and 500 for the employee ID
    while True:
        emp_id = random.randint(1, 500)
        # Check if ID already exists
        if emp_id not in existing_ids:
            break

    # Add the ID to the existing IDs list
    existing_ids.append(emp_id)

    # Create a dictionary for the new employee
    employee = {
        "name": name,
        "id": emp_id
    }

    # Add the employee dictionary to the employee list
    employee_list.append(employee)


# Main function
def main():
    print("This program records new employees and assigns each a unique ID number.\n")

    # Create empty lists for employees, IDs, and names
    employee_list = []      # List of dictionaries for employees
    existing_ids = []       # List to track existing employee ID numbers
    existing_names = []     # List to track existing employee names

    # Ask the user how many new employees to add
    while True:
        try:
            num_employees = int(input("Enter the number of new employees to add: "))
            if num_employees <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Loop to create new employees
    for i in range(num_employees):
        print(f"\n--- Adding Employee {i + 1} ---")
        create_employee(employee_list, existing_ids, existing_names)

    # Print the list of employees
    print("\nEmployee List:")
    for emp in employee_list:
        print(f"Name: {emp['name']}, ID: {emp['id']}")

    # Completion message
    print("\nCompleted by [Your Name Here]")


# Run the main function
if __name__ == "__main__":
    main()
