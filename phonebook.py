import json
import os

CONTACT_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list) and all(isinstance(contact, dict) for contact in data):
                    return data
                else:
                    print("⚠️ Invalid file format. Starting with empty contact list.")
                    return []
            except json.JSONDecodeError:
                print("⚠️ Could not read contacts.json. File may be corrupt.")
                return []
    return []


contact_list = load_contacts()


def save_contacts():
    with open(CONTACT_FILE, "w") as file:
        json.dump(contact_list, file, indent=4)
    print("✅ Contacts saved to file.")


def add_contact():
    name = input("\nWhat's your contact's name? ").lower()
    phone_number = input(
        "What's your contact's phone number? (format 000-000-0000) ")

    # Prevent duplicate names
    if any(contact["name"] == name for contact in contact_list):
        print("This contact already exists.\n")
        return

    new_contact = {
        "name": name,
        "phone": phone_number
    }

    contact_list.append(new_contact)
    save_contacts()  # Save after adding
    print(f"{name.title()} added successfully!\n")


def view_contacts():
    if not contact_list:
        print("\nYou don't have any contacts right now.\n")
    else:
        print("\nYour contacts:")
        # enumerate(..., 1) loops over the list and gives you:
        # idx: the index (starting from 1)
        # contact: each dictionary (like {"name": "alice", "phone": "123-456-7890"})
        for idx, contact in enumerate(contact_list, 1):
            # .title() formats the name in title case (e.g., "alice" → "Alice")
            print(f"{idx}. {contact['name'].title()} — {contact['phone']}")
        print()  # for spacing


def search_contact():
    name = input("What's the name of your contact? ").lower()
    found = False

    for contact in contact_list:
        if contact["name"] == name:
            print(
                f"\nContact found: {contact['name'].title()} — {contact['phone']}\n")
            found = True
            break

    if not found:
        print("\nContact not found.\n")


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
