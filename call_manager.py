python
# call_manager.py
from ui import display_menu, get_user_option, get_contact_info, show_contacts
from business_logic import ContactManager

def main():
    contact_manager = ContactManager()
    while True:
        display_menu()
        option = get_user_option()
        
        if option == '1':
            name, number = get_contact_info()
            contact_manager.add_contact(name, number)
            print(f"Contact '{name}' added successfully.")
        
        elif option == '2':
            contacts = contact_manager.view_contacts()
            show_contacts(contacts)
        
        elif option == '3':
            name = input("Enter the contact name to delete: ")
            contact_manager.delete_contact(name)
        
        elif option == '4':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
