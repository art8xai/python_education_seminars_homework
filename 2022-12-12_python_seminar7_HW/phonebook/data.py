def add_entry_file_csv(new_entry, file_path):
    """Add new entry to csv file."""
    with open(file_path, 'a', encoding='UTF-8') as file:
        file.write(
            f'Last Name: {new_entry[0]};'
            f'First Name: {new_entry[1]};'
            f'Phone number: {new_entry[2]};'
            f'Description: {new_entry[3]}\n')


def add_entry_file_txt(new_entry, file_path):
    """Add new entry to txt file."""
    with open(file_path, 'a', encoding='UTF-8') as file:
        file.write(f'Last Name: {new_entry[0]}\n'
                   f'First Name: {new_entry[1]}\n'
                   f'Phone number: {new_entry[2]}\n'
                   f'Description: {new_entry[3]}\n\n')
