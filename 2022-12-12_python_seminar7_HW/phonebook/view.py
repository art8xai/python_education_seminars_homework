def get_welcome():
    """Return the welcome."""
    return print('WELCOME TO PHONEBOOK!')


def get_menu():
    """Return main menu."""
    return int(input("""Menu:
1. New Entry
2. Display exiting contacts
3. Exit
Enter your choice here (1,2 or 3): """))


def set_new_entry():
    """Set up a new entry."""
    result = []
    last_name = input('Enter last name: ')
    result.append(last_name)
    first_name = input('Enter first name: ')
    result.append(first_name)
    phone_number = input('Enter phone number: ')
    result.append(phone_number)
    description = input('Enter a description: ')
    result.append(description)
    return result


def show_entries(file_path):
    """Show all existing entries."""
    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read()
