'''Модуль работы с данными телефонного справочника.'''

import json
from typing import List, Dict
from text import (contact_added, contact_exists, no_contact, no_idx_contact,
                  get_index, success_removal, value_error, change_name,
                  change_phone, change_tag, data_changed)



class ContactsInPhonebook:
    '''Класс для работы с контактами.'''

    def __init__(self, contacts):
        '''Инициализирует менеджер контактов

        Args:
            contacts: Список контактов для управления
        '''
        self.contacts = contacts

    def __str__(self):
        '''Возвращает строковое представление контактов.

        Returns:
            Строка со всеми контактами
        '''
        return str(self.contacts)

    def create_contact(self, new_contact: Dict[str, str]) -> List[Dict[str, str]]:
        '''Создание контакта.

        Args:
            new_contact: Словарь с данными нового контакта
        Добавляет контакт в список контактов self.contacts
        Returns:
            Сообщение о результате операции
        '''
        all_names = [contact['name'] for contact in self.contacts]

        if new_contact['name'] in all_names:
            return contact_exists

        else:
            self.contacts.append(new_contact)
            return contact_added

    def find_contact(self, find_data: str) -> List[Dict[str, str]]:
        '''Поиск контакта.

        Args:
            find_data: Строка с данными контакта
        Ищет совпадения в списке контактов self.contacts
        Returns:
            Сообщение о результате операции
        '''
        found_contact = []
        for contact in self.contacts:
            fields_to_check = ['name', 'phone', 'tag']
            for field in fields_to_check:
                if find_data.lower() in str(contact[field]).lower():
                    found_contact.append(contact)
                    break
        if len(found_contact) == 0:
            return no_contact
        else:
            return found_contact

    def change_by_index(self) -> int:
        '''Получает индекса контакта для дальнейшего изменения.

        Returns:
            int: Индекс контакта
        '''
        try:
            contact_for_change = get_index()
            if 1 <= contact_for_change <= len(self.contacts):
                return contact_for_change - 1
            else:
                return no_idx_contact
        except ValueError:
            return value_error

    def delete_contact(self):
        '''Удаляет контакт по полученному индексу change_by_index.'''
        del self.contacts[self.change_by_index()]
        return success_removal

    def change_contact(self, contact_index: int, field_choice: int) -> Dict:
        '''Измененяет данные контакта.

        Args:
            contact_index: Индекс изменяемого контакта
            field_choice: Номер поля для изменения (1-3)
        Изменяет словарь с данными контакта
        Returns:
            Сообщение о результате операции
        '''
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
    '''Файловый менеджер.'''

    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        '''Открывает файл.'''
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                file = json.load(f)
                return file
        except FileNotFoundError:
            print(f'Файл {self.filename} не найден. Создан новый файл.')
            return []
        except json.decoder.JSONDecodeError:
            print(f'Ошибка чтения JSON.')
            return []

    def save_file(self, contacts):
        '''Сохраняет файл.'''
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
