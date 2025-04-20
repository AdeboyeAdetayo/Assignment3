FILENAME = "contacts.txt"

def save_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    with open(FILENAME, 'a') as file:
        file.write(f"{name} - {phone}\n")
    print("Contact saved.")

def view_contacts():
    try:
        with open(FILENAME, 'r') as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
            for contact in contacts:
                print(contact.strip())
    except FileNotFoundError:
        print("No contact file found.")

while True:
    print("\n1. Save Contact\n2. View Contacts\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        save_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
