import json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

while True:
    print("\n--- Contact Book Menu ---")
    print(f"1. Add Contact\n2. Search Contact\n3.List All Contacts\n4.Delete Contact\n5.Exit")
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == '1':
        name = input("Enter contact name: ").strip()

        while True:
            phone = input("Enter contact phone number: ").strip()
            if len(phone) != 10:
                print("Phone number must be exactly 10 numeric digits long.")
                continue
            if not phone.isdigit():
                print("Phone number must contain only numeric digits.")
                continue
            break
        contacts[name] = phone
        print(f"Contact '{name}' added successfully.")
        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4)
    elif choice == '2':
        name = input("Enter contact name to search: ").strip()
        if name in contacts:
            print(f"Contact found: {name} - {contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")
    elif choice == '3':
        if contacts:
            print("All Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    elif choice == '4':
        name = input("Enter contact name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4)
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice or not implemented yet. Please try again.")