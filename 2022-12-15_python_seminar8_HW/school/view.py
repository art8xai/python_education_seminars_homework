def get_welcome():
    """Return the welcome."""
    return print('\nWELCOME TO THE SCHOOL DATABASE!')


def get_main_menu():
    """Return main menu."""
    return int(input("""\nMenu:
1. Teacher account
2. Student account
3. Exit
Enter your choice here (1,2 or 3): """))


def get_teacher_menu():
    """Return teacher menu."""
    return int(input("""\nMenu -> Teacher account:
1. Add student
2. Add subject grades to a student
3. Back to main menu
Enter your choice here (1,2 or 3): """))


def get_student_menu():
    """Return student menu."""
    return int(input("""\nMenu -> Student account:
1. Search by student's last name
2. Back to main menu
Enter your choice here (1 or 2): """))


def get_value_error_message():
    """Return a value error message."""
    print('Sorry, invalid input, please try again...')
