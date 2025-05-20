contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")

def search_contact():
    query = input("Search by Name or Phone: ")
    found = False
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['Phone']:
            print(f"\nName: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")
            found = True
    if not found:
        print("Contact not found!")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave blank to keep existing contact.")
        phone = input(f"New Phone ({contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"New Email ({contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"New Address ({contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print("Contact has been updated.")
    else:
        print("Contact not found!")

def del_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found!")

def menu():
    while True:
        print("\n********* Contact Book *******")
        print("I. Add Contact")
        print("II. View Contacts")
        print("III. Search Contact")
        print("IV. Update Contact")
        print("V. Delete Contact")
        print("VI. Exit")
        choice = input("Select an option: ")

        if choice == 'I':
            add_contact()
        elif choice == 'II':
            view_contacts()
        elif choice == 'III':
            search_contact()
        elif choice == 'IV':
            update_contact()
        elif choice == 'V':
            del_contact()
        elif choice == 'VI':
            print("Goodbye!")
            break
        else:
            print("Invalid option, Try again!")

menu()
