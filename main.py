'''Точка входа в приложение.'''

from controller import PhoneBook

phone_book = PhoneBook()

if __name__ == '__main__':
    phone_book.start_app()
