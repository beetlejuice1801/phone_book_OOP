import json
from text import contact_added, contact_exists, empty, no_contact, no_idx_contact


class ContactsInPhonebook:
    def __init__(self, contacts):
        self.contacts = contacts

    def __str__(self):
        return str(self.contacts)

    def create_contact(self, new_contact):
        all_names = [contact['name'] for contact in self.contacts]

        if new_contact['name'] in all_names:
            return contact_exists

        else:
            self.contacts.append(new_contact)
            return contact_added

    def find_contact(self, find_data):
        found_contact = []
        contacts_dict = dict(self.contacts.copy())
        for idx, contact in contacts_dict.items():
            if any(find_data.lower() in str(contact[field]).lower() for field in ['name', 'phone', 'tag']):
                found_contact.append(contact)
            else:
                return no_contact
        return found_contact

    def delete_contact(self):
        try:
            contact_for_delete = text.get_index_for_delete()
            if 1 <= contact_for_delete <= len(self.contacts):
                del self.contacts[contact_for_delete - 1]
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
            file = json.load(f)
            return file

    def save_file(self, contacts):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
