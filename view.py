'''Модуль пользовательского интерфейса телефонного справочника.'''

from typing import Optional, Tuple, List, Dict
import re
from prettytable import PrettyTable
import text


class Interface:
    '''Класс, отвечающий за пользовательский ввод и отображение.'''

    def __init__(self, data):
        self.data = data

    NAME_PATTERN = r'^[A-ZА-ЯЁ][a-zа-яё]+(?:\s[A-ZА-ЯЁ][a-zа-яё]+)*$'

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, Optional[str], Optional[str]]:
        '''Валидация ввода имени.

        Args:
            name: Имя для валидации
        Returns:
            Кортеж(успех, сообщение об ошибке, исправленное имя)
        '''
        if not name or not name.strip():
            err_msg = 'Поле не может быть пустым'
            return False, err_msg, None

        cleaned = name.strip()

        if len(cleaned) > 40:
            err_msg = 'Имя слишком длинное'
            return False, err_msg, None

        corrected_name = name.title()

        if not re.match(Interface.NAME_PATTERN, corrected_name):
            err_msg = 'Имя может содержать только буквы и пробелы'
            return False, err_msg, None

        return True, None, corrected_name

    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, Optional[str], Optional[str]]:
        '''Валидация ввода номера.

        Args:
            phone: Номер для валидации
        Returns:
            Кортеж(успех, сообщение об ошибке, исправленный номер)
        '''
        if not phone or not phone.strip():
            err_msg = 'Поле не может быть пустым.'
            return False, err_msg, None

        cleaned = re.sub(r'[^\d+]', '', phone.strip())

        if len(cleaned) < 11:
            err_msg = 'Номер телефона слишком короткий.'
            err_msg += 'Используйте формат 7YYYXXXCCZZ.'
            return False, err_msg, None

        if len(cleaned) > 16:
            err_msg = 'Номер телефона слишком длинный.'
            err_msg += 'Используйте формат 7YYYXXXCCZZ.'
            return False, err_msg, None

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
            err_msg = 'Неверный формат. Номер должен содержать 11 цифр. '
            err_msg += f'Сейчас: {len(corrected_phone)}.'
            return False, err_msg, None

        if not corrected_phone.isdigit():
            err_msg = 'Номер должен содержать только цифры.'
            return False, err_msg, None

        return True, None, corrected_phone

    @staticmethod
    def beautiful_show(contacts: List[Dict[str, any]]) -> str:
        '''Табличное отображение контактов.

        Args:
            contacts: Список контактов
        Returns:
            Таблица в виде строки
        '''
        my_table = PrettyTable()
        my_table.field_names = ['Номер', 'Имя', 'Телефон', 'Кто таков']
        for idx, val in enumerate(contacts, start=1):
            idx = int(idx)
            row = [idx, val['name'], val['phone'], val['tag']]
            my_table.add_row(row)
        return my_table.get_string()

    @staticmethod
    def user_input():
        '''Пользовательский ввод для создания контакта.

        Returns:
            Словарь с данными контакта
        '''
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
        '''Выбор пункта меню.

        Returns:
            int: Выбранный пункт меню
        '''
        while True:
            main_menu_choice = input(text.main_menu_choice)
            if main_menu_choice.isdigit() and 1 <= int(main_menu_choice) <= len(text.main_menu):
                return int(main_menu_choice)
            else:
                print(text.main_menu_error)

    @staticmethod
    def user_choice_for_edit() -> int:
        '''Выбор поля для изменения контакта.

        Returns:
            int: Выбранное поле для изменения
        '''
        while True:
            user_choice = text.get_field()
            if user_choice.isdigit() and 1 <= int(user_choice) <= 3:
                return int(user_choice)
            else:
                print(text.field_error)

    @staticmethod
    def show_menu(data):
        '''Отображение главного меню.'''
        for idx, paragraph in enumerate(data, start=1):
            print(f'{idx}. {paragraph}')
