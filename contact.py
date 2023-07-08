import csv

contacts = []

def add_contact(name, email, phone):
    contact = [name, email, phone]
    contacts.append(contact)
    print("Contact added successfully!")

def update_contact(name, email, phone):
    for contact in contacts:
        if contact[0] == name:
            contact[1] = email
            contact[2] = phone
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact[0] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def display_contacts():
    if contacts:
        for contact in contacts:
            print(f"Name: {contact[0]}, Email: {contact[1]}, Phone: {contact[2]}")
    else:
        print("No contacts found.")

def save_contacts_to_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone"])
        writer.writerows(contacts)
    print(f"Contacts saved to {filename} successfully!")

def load_contacts_from_csv(filename):
    contacts.clear()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            contacts.append(row)
    print(f"Contacts loaded from {filename} successfully!")

while True:
    print("\n--- Contact Management System ---\n")
    print("1. Add Contact\n")
    print("2. Update Contact\n")
    print("3. Delete Contact\n")
    print("4. Display Contacts\n")
    print("5. Save Contacts to CSV\n")
    print("6. Load Contacts from CSV\n")
    print("7. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        add_contact(name, email, phone)

    elif choice == '2':
        name = input("Enter name: ")
        email = input("Enter new email: ")
        phone = input("Enter new phone: ")
        update_contact(name, email, phone)

    elif choice == '3':
        name = input("Enter name: ")
        delete_contact(name)

    elif choice == '4':
        display_contacts()

    elif choice == '5':
        filename = input("Enter the filename to save contacts: ")+ ".csv"
        save_contacts_to_csv(filename)

    elif choice == '6':
        filename = input("Enter the filename to load contacts: ")+ ".csv"
        load_contacts_from_csv(filename)

    elif choice == '7':
        break

    else:
        print("Invalid choice. Please try again.")