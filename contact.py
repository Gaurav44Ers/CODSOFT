class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone_number, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'Phone': phone_number, 'Email': email, 'Address': address}
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists. Use update_contact to modify details.")
    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            print()
    def search_contact(self, search_term):
        search_results = []
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['Phone']:
                search_results.append((name, details))
        return search_results
    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {'Phone': phone_number, 'Email': email, 'Address': address}
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} does not exist. Use add_contact to add a new contact.")
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} does not exist.")


contact_book = ContactBook()
contact_book.add_contact("Gaurav", "8808645481", "gaurav1@gmail.com", "patel nagar")
contact_book.add_contact("Rishabh", "8808645482", "rishabh2@gmail.com", "anand nagar")
contact_book.view_contact_list()


search_term = input("Enter a name or phone number to search: ")
search_results = contact_book.search_contact(search_term)
if search_results:
    print("\nSearch Results:")
    for name, details in search_results:
        print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
else:
    print("No matching contacts found.")


contact_book.update_contact("Gaurav", "1234567891", "gaurav1@gmail.com", "thakral nagar")
contact_book.delete_contact("Rishabh")
contact_book.view_contact_list()
