
contact_exists = 'Такой контакт уже существует!'
contact_added = 'Контакт успешно добавлен!'
empty = 'Телефонная книга пуста'
contact_search_data = input('Введите имя контакта, номер телефона или комментарий для поиска по справочнику: ')
no_contact = 'Контакт отсутствует!'
no_idx_contact = 'Контакт по такому индексу не найден'
val_err = 'Введите числовое значение!'
sucess_remove = 'Контакт успешно удалён'







class Interface:
    def __init__(self, data):
        self.data = data

    def beautiful_show(self):
        my_table = PrettyTable()
        my_table.field_names = ['Номер', 'Имя', 'Телефон', 'Кто таков']
        for idx, val in self.data.items():
            idx = str(idx)
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
