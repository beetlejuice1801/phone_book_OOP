import text
from prettytable import PrettyTable
import re
from typing import Optional, Tuple


class Interface:
    def __init__(self, data):
        self.data = data

    NAME_PATTERN = r'^[A-ZА-ЯЁ][a-zа-яё]+(?:\s[A-ZА-ЯЁ][a-zа-яё]+)*$'

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, Optional[str], Optional[str]]:

        '''Валидация ввода имени'''

        if not name or not name.strip():
            return False, 'Поле не может быть пустым', None

        cleaned = name.strip()

        if len(cleaned) > 40:
            return False, 'Имя слишком длинное', None

        corrected_name = name.title()

        if not re.match(Interface.NAME_PATTERN, corrected_name):
            return False, 'Имя может содержать только буквы и пробелы', None

        return True, None, corrected_name

    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, Optional[str], Optional[str]]:

        '''Валидация ввода номера'''

        if not phone or not phone.strip():
            return False, 'Поле не может быть пустым', None

        cleaned = re.sub(r'[^\d+]', '', phone.strip())

        if len(cleaned) < 11:
            return False, 'Номер телефона слишком короткий. Используйте формат 7YYYXXXCCZZ', None
        if len(cleaned) > 16:
            return False, 'Номер телефона слишком длинный. Используйте формат 7YYYXXXCCZZ', None

        if cleaned.startswith('8'):
            corrected_phone = '7' + cleaned[1:]
        elif cleaned.startswith('+7'):
            corrected_phone = cleaned[2:]
            corrected_phone = '7' + corrected_phone
        elif len(cleaned) == 10:
            corrected_phone = '7' + cleaned
        elif cleaned.startswith('7'):
            corrected_phone = cleaned
        else:
            return False, 'Неверный формат', None

        if len(corrected_phone) != 11:
            return False, f'Неверный формат. Номер должен содержать 11 цифр. Сейчас: {len(corrected_phone)}', None

        if not corrected_phone.isdigit():
            return False, 'Номер должен содержать только цифры', None

        return True, None, corrected_phone

    @staticmethod
    def beautiful_show(contacts: list[dict[str, any]]):

        '''Табличное отображение контактов'''

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
            valid_name, error, correct_name = Interface.validate_name(name)
            if valid_name:
                name = correct_name
                break
            print(f'Ошибка: {error}')

        while True:
            phone = input('Введите номер телефона контакта: ')
            valid_phone, error, correct_phone = Interface.validate_phone(phone)
            if valid_phone:
                phone = correct_phone
                break
            print(f'Ошибка: {error}')

        tag = input('Введите комментарий: ')
        return {'name': name, 'phone': phone, 'tag': tag}


    @staticmethod
    def user_menu_choice() -> int:

        '''Выбор пункта меню'''

        while True:
            main_menu_choice = input(text.main_menu_choice)
            if main_menu_choice.isdigit() and 1 <= int(main_menu_choice) <= len(text.main_menu):
                return int(main_menu_choice)
            else:
                print(text.main_menu_error)

    @staticmethod
    def user_choice_for_edit() -> int:

        '''Выбор поля для изменения контакта'''

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
