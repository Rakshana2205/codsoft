contacts = []

def add_contact():
    print("\nAdd Contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    print("\nContact List:")
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

def search_contact():
    print("\nSearch Contact:")
    search_term = input("Enter name or phone number to search: ")
    search_results = []

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            search_results.append(contact)

    if search_results:
        print("Search Results:")
        for result in search_results:
            print(f"{result['Name']} - {result['Phone']}")
    else:
        print("No matching contacts found.")

def update_contact():
    view_contact_list()
    try:
        contact_index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= contact_index < len(contacts):
            print("\nUpdate Contact:")
            contacts[contact_index]['Name'] = input("Enter new name: ")
            contacts[contact_index]['Phone'] = input("Enter new phone number: ")
            contacts[contact_index]['Email'] = input("Enter new email: ")
            contacts[contact_index]['Address'] = input("Enter new address: ")
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact():
    view_contact_list()
    try:
        contact_index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            deleted_contact = contacts.pop(contact_index)
            print(f"Contact {deleted_contact['Name']} - {deleted_contact['Phone']} deleted successfully!")
        else:
            print("Invalid contact index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Quit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contact_list()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                update_contact()
            elif choice == 5:
                delete_contact()
            elif choice == 6:
                print("Exiting the Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
