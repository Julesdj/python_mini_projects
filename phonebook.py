from phonebook_utils import add_contact, view_contacts, search_contact, save_contacts

options = {
    1: "Add a new contact.",
    2: "View contact list.",
    3: "Find a contact.",
    4: "Done, quit the program.\n"
}

while True:
    print("What would you like to do today?")
    for key, value in options.items():
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
            print("\nGoodbye!\n")
            break
        else:
            print("\nNot a valid option, try again.\n")
    except ValueError:
        print("\nPlease enter a number.\n")
