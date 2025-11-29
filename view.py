import text
from prettytable import PrettyTable




class Interface:
    def __init__(self, data):
        self.data = data


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
        name = input('Введите имя контакта: ')
        while True:
            try:
                phone = int(input('Введите номер телефона контакта: '))
                break
            except ValueError:
                print('Введите корректный номер телефона - 7999xxxxxxx')
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
    def show_menu():
        for idx, paragraph in enumerate(text.main_menu, start=1):
            print(f'{idx}. {paragraph}')

