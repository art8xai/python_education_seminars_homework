import data
import view

file_csv_path = 'data/phonebook.csv'
file_txt_path = 'data/phonebook.txt'


def start():
    """Start the program."""
    view.get_welcome()
    while True:
        try:
            menu_choice = view.get_menu()
        except ValueError:
            print('Sorry, invalid input, please try again...')
            continue
        else:
            match menu_choice:
                case 1:
                    new_entry = view.set_new_entry()
                    data.add_entry_file_csv(new_entry, file_csv_path)
                    data.add_entry_file_txt(new_entry, file_txt_path)
                    print('The export of data to a file is complete.')
                case 2:
                    print(view.show_entries(file_csv_path))
                    print('The import of data from the file is complete.')
                case 3:
                    print('Thank you for using the phonebook!')
                    break
                case _:
                    print('Sorry, invalid input, please try again...')
                    continue
