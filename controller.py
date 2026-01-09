'''Модуль контроллера для телефонного справочника.'''

import view
import model
import text


class PhoneBook:
    '''Основной класс управления телефонным справочником.'''

    def __init__(self):
        '''Инициализация телефонного справочника.'''
        self.contacts_from_file = []
        self.phone_book_manager = None

    def _checking_phone_book(self):
        '''Проверка, что телефонная книга загружена.'''
        if self.phone_book_manager is None:
            print(text.no_phone_manager)
            return False
        return True

    def start_app(self):
        '''Запуск основного меню приложения.'''
        while True:
            view.Interface.show_menu(text.main_menu)
            user_choice = view.Interface.user_menu_choice()

            if user_choice == 1:
                self._open_file()

            elif user_choice == 2:
                self._save_file()

            elif user_choice == 3:
                self._show_all_contacts()

            elif user_choice == 4:
                self._create_contact()

            elif user_choice == 5:
                self._find_contact()

            elif user_choice == 6:
                self._change_contact()

            elif user_choice == 7:
                self._delete_contact()

            else:
                exit()

    def _open_file(self) -> None:
        '''Открывает файл с контактами.'''
        filemanager = model.FileManager('data.json')
        self.contacts_from_file = filemanager.open_file()
        self.phone_book_manager = model.ContactsInPhonebook(
            self.contacts_from_file)
        print(text.file_opened)

    def _save_file(self) -> None:
        '''Сохраняет файл.'''
        filemanager = model.FileManager('data.json')
        filemanager.save_file(self.contacts_from_file)
        print(text.file_saved)

    def _show_all_contacts(self) -> None:
        '''Отображает все контакты.'''
        if self._checking_phone_book():
            interface = view.Interface(self.contacts_from_file)
            print(interface.beautiful_show(self.contacts_from_file))


    def _create_contact(self) -> None:
        '''Создаёт новый контакт.'''
        if self._checking_phone_book():
            new_data = view.Interface.user_input()
            result = self.phone_book_manager.create_contact(new_data)
            self.contacts_from_file = self.phone_book_manager.contacts
            print(result)

    def _find_contact(self) -> None:
        '''Поиск контакта.'''
        if self._checking_phone_book():
            result = self.phone_book_manager.find_contact(
                text.get_contact_search_data())
            print(view.Interface.beautiful_show(result))

    def _change_contact(self) -> None:
        '''Измененяет контакт.'''
        if self._checking_phone_book():
            index = self.phone_book_manager.change_by_index()
            if isinstance(index, int):
                field_choice = view.Interface.user_choice_for_edit()
                self.phone_book_manager.change_contact(index, field_choice)
                print(text.data_changed)
            else:
                print(text.no_idx_contact)

    def _delete_contact(self) -> None:
        '''Удаляет контакт.'''
        result = model.ContactsInPhonebook(self.contacts_from_file)
        print(result.delete_contact())
