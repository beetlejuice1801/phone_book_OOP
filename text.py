main_menu = [
    'Открыть файл',
    'Сохранить файл',
    'Показать все контакты',
    'Создать контакт',
    'Найти контакт',
    'Изменить контакт',
    'Удалить контакт'

]
contact_exists = '\nТакой контакт уже существует!\n'
contact_added = '\nКонтакт успешно добавлен!\n'
empty = '\nТелефонная книга пуста\n'
no_contact = '\nКонтакт отсутствует!\n'
no_idx_contact = '\nКонтакт по такому индексу не найден\n'
val_err = '\nВведите числовое значение!\n'
sucess_remove = '\nКонтакт успешно удалён\n'
main_menu_choice = f'\nВыберите пункт меню: '
main_menu_error = f'\nВыберите от 1 до {len(main_menu)}'
file_opened = '\nТелефонная книга открыта\n'
file_saved = '\nТелефонная книга сохранена\n'
no_phone_manager = '\nТелефонная книга не загружена\n'
field_error = '\nВыберите от 1 до 3\n'
data_changed = '\nДанные успешно изменены\n'




def get_contact_search_data():
    return input('\nВведите имя контакта, номер телефона или комментарий для поиска по справочнику: \n')

def get_index():
    return int(input('\nВведите индекс контакта: \n'))

def get_field():
    return input('\nВведите, что хотите изменить(цифрой)\n 1. Имя | 2. Номер | 3. Комментарий\n')

def change_name():
    return input('\nВведите новое имя: \n')

def change_phone():
    return int(input('\nВведите новый номер: \n'))

def change_tag():
    return input('\nВведите новый комментарий: \n')

