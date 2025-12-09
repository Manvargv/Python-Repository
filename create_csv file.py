def create_csv_file(filename):
    with open(filename, "w") as file:
        file.write("Name,Phone,Email\n")
    print(f"\nFile '{filename}' created successfully!\n")


def add_contact(filename):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    with open(filename, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print(f"\nContact '{name}' added successfully!\n")


def view_contacts(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) <= 1:
            print("\nNo contacts found.\n")
            return

        print("\n--- Contact List ---")
        for line in lines:
            print(line.strip())
        print()
    except FileNotFoundError:
        print("\nNo contact file found. Please create one first.\n")


def edit_contact(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) <= 1:
            print("\nNo contacts to edit.\n")
            return

        print("\n--- Existing Contacts ---")
        for i in range(1, len(lines)):
            print(f"{i}. {lines[i].strip()}")

        choice = input("\nEnter the number of the contact to edit: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) >= len(lines):
            print("\nInvalid choice.\n")
            return

        index = int(choice)
        parts = lines[index].strip().split(',')
        print(f"Editing contact: {parts[0]}")

        new_phone = input("Enter new phone: ")
        new_email = input("Enter new email: ")

        lines[index] = f"{parts[0]},{new_phone},{new_email}\n"

        with open(filename, "w") as file:
            file.writelines(lines)

        print(f"\nContact '{parts[0]}' updated successfully!\n")

    except FileNotFoundError:
        print("\nNo contact file found. Please create one first.\n")


def main():
    print("Welcome to the Simple Contact Management Program!")
    filename = "contacts.csv"

    while True:
        print("1 - Create new contact CSV file")
        print("2 - Add a new contact")
        print("3 - View all contacts")
        print("4 - Edit an existing contact")
        print("5 - Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_csv_file(filename)
        elif choice == "2":
            add_contact(filename)
        elif choice == "3":
            view_contacts(filename)
        elif choice == "4":
            edit_contact(filename)
        elif choice == "5":
            print("\nExiting program. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

    print("Completed by, [Manuel Vargas]") 


if __name__ == "__main__":
    main()
