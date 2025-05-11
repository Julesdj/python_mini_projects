import json
import os
import csv
from contact_model import Contact

JSON_CONTACT_FILE = "contacts.json"
CSV_CONTACT_FILE = "contacts.csv"


contact_list = []


def load_contacts():  # Load existing contacts from the json file
    global contact_list
    if os.path.exists(JSON_CONTACT_FILE):
        with open(JSON_CONTACT_FILE, "r") as file:
            try:
                data = json.load(file)
                contact_list = [Contact.from_dict(contact) for contact in data]
                print(f"✅ Loaded {len(contact_list)} contacts.")
            except json.JSONDecodeError:
                print(
                    "⚠️ Could not read contacts.json. Starting with empty contact list.")
                contact_list = []


def save_contacts():  # Save contacts to Json file
    with open(JSON_CONTACT_FILE, "w") as file:
        json.dump([contact.to_dict()
                  for contact in contact_list], file, indent=4)
    print("\n✅ Contacts saved to json file.")


def save_contacts_to_csv():
    with open(CSV_CONTACT_FILE, "w", newline="") as csvfile:
        fieldnames = ["name", "phone"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows([contact.to_dict() for contact in contact_list])
    print("\n✅ Contacts saved to csv file.")


def read_csv_contacts():
    if os.path.exists(CSV_CONTACT_FILE):
        with open(CSV_CONTACT_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            print("📂 Contacts from CSV:")
            # next(reader)  # Skip header
            for row in reader:
                print(f"Name: {row["name"].title()}, Phone: {row["phone"]}")
    else:
        print("❌ No CSV file found.")


def add_contact():
    name = input("\nWhat's your contact's name? ").lower()
    if not name or len(name) > 30:
        print("❌ Invalid name. Must be 1–30 characters.")
        return

    while True:
        raw_phone = input(
            "Enter phone number?: ").strip()
        temp = Contact(name, raw_phone)

        if temp.phone:
            break
        else:
            print("❌ Invalid phone number. Use 123-456-7890 format.")

    # Duplicate check
    if any(contact.name == name for contact in contact_list):
        print("This contact already exists.\n")
        return

    contact_list.append(temp)
    save_contacts()  # Save after adding
    save_contacts_to_csv()
    print(f"{name.title()} added successfully!\n")


def view_contacts():
    if not contact_list:
        print("\nYou don't have any contacts right now.\n")
        return
    print("\n📒 Your Contacts:")
    for idx, ccontact in enumerate(contact_list, 1):
        print(f"{idx}. ", end="")
        ccontact.display()
    print()
    read_csv_contacts()


def search_contact():
    name = input("Enter the contact name to search: ").lower()

    for contact in contact_list:
        if contact.name == name:
            print("\n🔍 Contact found:")
            contact.display()
            return
    print("\n❌ Contact not found.")
