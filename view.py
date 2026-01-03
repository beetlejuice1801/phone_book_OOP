import text
from prettytable import PrettyTable
import re
from typing import Optional, Tuple


class Interface:
    def __init__(self, data):
        self.data = data

    NAME_PATTERN = r'^[A-ZА-ЯЁ][a-zа-яё]+(?:\s[A-ZА-ЯЁ][a-zа-яё]+)*$'
    PHONE_PATTERN = r'^(\+7|7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, Optional[str]]:
        if not name or not name.strip():
            return False, 'Поле не может быть пустым'

        if len(name) > 70:
            return False, 'Имя слишком длинное'

        if not re.match(Interface.NAME_PATTERN, name.title()):
            return False, 'Имя может содержать только буквы и пробелы'

        return True, None

    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, Optional[str]]:
        if not phone or not phone.strip():
            return False, 'Поле не может быть пустым'

        correct_phone = re.sub(r'[^\d+]', '', phone.strip())

        if len(correct_phone) < 10:
            return False, 'Номер телефона слишком короткий'

        if len(correct_phone) > 16:
            return False, 'Номер телефона слишком длинный'

        if not re.match(r'^(\+7|7|8)\d{10}$', correct_phone):
            if correct_phone.startswith('8'):
                correct_phone = '7' + correct_phone[1::]
            elif correct_phone.startswith('+7'):
                correct_phone = '7' + correct_phone[2::]
            elif correct_phone == 10:
                correct_phone += '7'
            else:
                return False, 'Неверный формат. Используйте +7XXXCCCYYZZ'

        if len(correct_phone) != 11:
            return False, f'Неверный формат. Номер должен содержать 11 цифр. Сейчас {len(correct_phone)}'

        return True, None

    @staticmethod
    def beautiful_show(contacts):
        my_table = PrettyTable()
        my_table.field_names = ['Номер', 'Имя', 'Телефон', 'Кто таков']
        for idx, val in enumerate(contacts, start=1):
            idx = int(idx)
            row = [idx, val['name'], val['phone'], val['tag']]
            my_table.add_row(row)
        return my_table.get_string()

    @staticmethod
    def user_input():
        while True:
            name = input('Введите имя контакта: ')
            valid_name, error = Interface.validate_name(name)
            if valid_name:
                break
            print(f'Ошибка: {error}')

        while True:
            phone = (input('Введите номер телефона контакта: '))
            valid_phone, error = Interface.validate_phone(phone)
            if valid_phone:
                break
            print(f'Ошибка: {error}')

        tag = input('Введите комментарий: ')
        return {'name': name, 'phone': phone, 'tag': tag}

    @staticmethod
    def index_for_contacts(contacts):
        final_result = {}
        for idx, contact in enumerate(contacts, start=1):
            final_result[idx] = contact
        return final_result

    @staticmethod
    def user_menu_choice():
        while True:
            main_menu_choice = input(text.main_menu_choice)
            if main_menu_choice.isdigit() and 1 <= int(main_menu_choice) <= len(text.main_menu):
                return int(main_menu_choice)
            else:
                print(text.main_menu_error)

    @staticmethod
    def user_choice_for_edit():
        while True:
            user_choice = text.get_field()
            if user_choice.isdigit() and 1 <= int(user_choice) <= 3:
                return int(user_choice)
            else:
                print(text.field_error)

    @staticmethod
    def show_menu(data):
        for idx, paragraph in enumerate(data, start=1):
            print(f'{idx}. {paragraph}')
