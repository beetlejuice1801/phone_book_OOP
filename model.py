import json

from view import contact_search_data, no_contact


class ContactsInPhonebook:
    def __init__(self, contacts):
        self.contacts = {}
        for idx, contact in enumerate(contacts, start=1):
            self.contacts[idx] = contact

    def __str__(self):
        return str(self.contacts)

    def create_contact(self, new_contact):
        try:
            next_idx = max(self.contacts.keys()) + 1
        except ValueError:
            return empty

        all_names = [contact['name'] for contact in self.contacts.values()]

        if new_contact['name'] in all_names:
            return contact_exists
        else:
            self.contacts[next_idx] = new_contact
            return contact_added

    def find_contact(self, find_data):
        found_contact = []
        for idx, contact in self.contacts.items():
            if any(find_data.lower() in str(contact[field]).lower() for field in ['name', 'phone', 'tag']):
                found_contact.append(contact)
            else:
                return no_contact
        return beautiful

    def delete_contact(self):
        try:
            contact_for_delete = int(input('Введите индекс контакта, который хотите удалить: '))
            if 0 <= contact_for_delete <= len(self.contacts):
                del self.contacts[contact_for_delete]
            else:
                return no_idx_contact
        except ValueError:
            return val_err
        return sucess_remove


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_file(self, contacts):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)


file = FileManager('data.json')
contacts_from_file = file.open_file()
enumerate_contacts = ContactsInPhonebook(contacts_from_file)
poisk_contacta = enumerate_contacts.find_contact(contact_search_data)
print(poisk_contacta)
