from phonebook_utils import add_contact, view_contacts, search_contact, load_contacts


def phonebook():
    load_contacts()  # Load from JSON file at startup

    menu = {
        1: "Add a new contact",
        2: "View contact list",
        3: "Find a contact",
        4: "Quit\n"
    }

    while True:
        print("\nWhat would you like to do today?")
        for key, value in menu.items():
            print(f"{key}: {value}")

        try:
            command = int(input("Choose an option: "))
            if command == 1:
                add_contact()
            elif command == 2:
                view_contacts()
            elif command == 3:
                search_contact()
            elif command == 4:
                print("\n👋 Goodbye!\n")
                break
            else:
                print("\nInvalid choice, try again.\n")
        except ValueError:
            print("\nPlease enter a valid number.\n")


if __name__ == "__main__":
    phonebook()
