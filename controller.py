import view
import model
import text


class PhoneBook:
    def __init__(self):
        self.contacts_from_file = []
        self.phone_book_manager = None

    def start_app(self):
        while True:
            view.Interface.show_menu(text.main_menu)
            user_choice = view.Interface.user_menu_choice()

            if user_choice == 1:
                filemanager = model.FileManager('data.json')
                self.contacts_from_file = filemanager.open_file()
                self.phone_book_manager = model.ContactsInPhonebook(self.contacts_from_file)
                print(text.file_opened)

            elif user_choice == 2:
                filemanager = model.FileManager('data.json')
                filemanager.save_file(self.contacts_from_file)
                print(text.file_saved)

            elif user_choice == 3:
                if self.phone_book_manager is None:
                    print(text.no_phone_manager)
                else:
                    interface = view.Interface(self.contacts_from_file)
                    print(interface.beautiful_show(self.contacts_from_file))

            elif user_choice == 4:
                if self.phone_book_manager is None:
                    print(text.no_phone_manager)

                else:
                    new_data = view.Interface.user_input()
                    result = self.phone_book_manager.create_contact(new_data)
                    self.contacts_from_file = self.phone_book_manager.contacts
                    print(result)

            elif user_choice == 5:
                if self.phone_book_manager is None:
                    print(text.no_phone_manager)
                else:
                    result = self.phone_book_manager.find_contact(text.get_contact_search_data())
                    print(view.Interface.beautiful_show(result))

            elif user_choice == 6:
                if self.phone_book_manager is None:
                    print(text.no_phone_manager)
                else:
                    index = self.phone_book_manager.change_by_index()
                    if isinstance(index, int):
                        field_choice = view.Interface.user_choice_for_edit()
                        self.phone_book_manager.change_contact(index, field_choice)
                        print(text.data_changed)
                    else:
                        print(text.no_idx_contact)


            elif user_choice == 7:
                result = model.ContactsInPhonebook(self.contacts_from_file)
                print(result.delete_contact())

            else:
                exit()
