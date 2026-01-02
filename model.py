import json
from text import contact_added, contact_exists, empty, no_contact, no_idx_contact
from text import get_index, sucess_remove, val_err, change_name, change_phone, change_tag, data_changed


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
        for contact in self.contacts:
            if any(find_data.lower() in str(contact[field]).lower() for field in ['name', 'phone', 'tag']):
                found_contact.append(contact)
        if len(found_contact) == 0:
            return no_contact
        else:
            return found_contact

    def change_by_index(self):
        try:
            contact_for_change = get_index()
            if 1 <= contact_for_change <= len(self.contacts):
                return contact_for_change - 1
            else:
                return no_idx_contact
        except ValueError:
            return val_err

    def delete_contact(self):
        del self.contacts[self.change_by_index()]
        return sucess_remove

    def change_contact(self, contact_index, field_choice):
        if not (0 <= contact_index < len(self.contacts)):
            return no_idx_contact
        contact_to_change = self.contacts[contact_index]
        values_list = list(contact_to_change.values())

        if field_choice == 1:
            name = change_name()
            values_list[0] = name
        elif field_choice == 2:
            phone = change_phone()
            values_list[1] = phone
        elif field_choice == 3:
            tag = change_tag()
            values_list[2] = tag

        contact_to_change['name'] = values_list[0]
        contact_to_change['phone'] = values_list[1]
        contact_to_change['tag'] = values_list[2]

        return data_changed


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
