contacts = []

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        contacts.append(contact)
        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n------ Contact List ------")
            for contact in contacts:
                print(f"Name    : {contact['Name']}")
                print(f"Phone   : {contact['Phone']}")
                print(f"Email   : {contact['Email']}")
                print(f"Address : {contact['Address']}")
                print("---------------------------")

    # Search Contact
    elif choice == "3":
        search = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["Name"].lower() == search.lower():
                print("\nContact Found")
                print(f"Name    : {contact['Name']}")
                print(f"Phone   : {contact['Phone']}")
                print(f"Email   : {contact['Email']}")
                print(f"Address : {contact['Address']}")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        update = input("Enter name to update: ")

        found = False

        for contact in contacts:
            if contact["Name"].lower() == update.lower():
                contact["Phone"] = input("Enter New Phone: ")
                contact["Email"] = input("Enter New Email: ")
                contact["Address"] = input("Enter New Address: ")
                print(" Contact updated successfully!")
                found = True
                break

        if not found:
            print(" Contact not found.")

    # Delete Contact
    elif choice == "5":
        delete = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact["Name"].lower() == delete.lower():
                contacts.remove(contact)
                print(" Contact deleted successfully!")
                found = True
                break

        if not found:
            print(" Contact not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using the Contact Book!")
        break

    else:
        print(" Invalid choice! Please enter a number from 1 to 6.")