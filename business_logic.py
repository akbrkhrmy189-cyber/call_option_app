
```python
# business_logic.py
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def view_contacts(self):
        return self.contacts

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print(f"Contact '{name}' not found.")
```
