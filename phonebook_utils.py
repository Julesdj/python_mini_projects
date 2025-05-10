import json
import os
import re
import csv

JSON_CONTACT_FILE = "contacts.json"
CSV_CONTACT_FILE = "contacts.csv"


# Phone number formating using Regex: US style only
def normalize_phone_number(raw_phone_number):
    # Remove anything that's not a digit
    digits = re.sub(r"[^\d]", "", raw_phone_number)

    # Remove leading country code if it's +1 or 1
    if digits.startswith("1") and len(digits) == 11:
        digits = digits[1:]

    if len(digits) == 10:
        # Return in 123-456-7890 format
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    else:
        return None


def load_contacts():  # Load existing contacts from the json file
    if os.path.exists(JSON_CONTACT_FILE):
        with open(JSON_CONTACT_FILE, "r") as file:
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


def read_csv_contacts():
    if os.path.exists(CSV_CONTACT_FILE):
        with open(CSV_CONTACT_FILE, "r") as csvfile:
            reader = csv.reader(csvfile)
            print("Your contacts in CSV:")
            next(reader)  # Skip header
            for row in reader:
                print(f"Name: {row[0].title()}, Phone: {row[1]}")

            # Here's how to use DictReader insteat
            # dictreader = csv.DictReader(csvfile)
            # for row in dictreader:
            #     print(f"Name: {row['name'].title()}, Phone: {row['phone']}")
    else:
        print("❌ No CSV file found.")


contact_list = load_contacts()


def save_contacts():  # Save contacts to Json file
    with open(JSON_CONTACT_FILE, "w") as file:
        json.dump(contact_list, file, indent=4)
    print("\n✅ Contacts saved to json file.")


def save_contacts_to_csv(contacts):
    with open(CSV_CONTACT_FILE, "w", newline="") as csvfile:
        fieldnames = ["name", "phone"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(contacts)
    print("✅ Contacts saved to csv file.")


def add_contact():
    name = input("\nWhat's your contact's name? ").lower()
    if len(name) == 0:
        print("\n❌ Name must be at least one character long.\n")
        return

    if len(name) > 10:
        print("\n❌ Name is too long.\n")
        return

    while True:
        raw_phone_number = input(
            "What's your contact's phone number?: ").strip()
        phone_number = normalize_phone_number(raw_phone_number)
        if phone_number:
            break
        else:
            print("❌ Invalid phone number. Please enter a valid US-style number.")

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
    save_contacts_to_csv(contacts=contact_list)
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

    read_csv_contacts()


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
