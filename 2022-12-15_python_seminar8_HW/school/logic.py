import data
import student
import teacher
import view

file_path = 'data/db_student.json'


def start():
    """Start the program."""
    view.get_welcome()
    data.db_load(file_path)
    while True:
        try:
            menu_choice = view.get_main_menu()
        except ValueError:
            view.get_value_error_message()
            continue
        else:
            match menu_choice:
                # Teacher account.
                case 1:
                    while True:
                        try:
                            teacher_choice = view.get_teacher_menu()
                        except ValueError:
                            view.get_value_error_message()
                            continue
                        else:
                            match teacher_choice:
                                case 1:
                                    teacher.add_student()
                                case 2:
                                    teacher.add_rating()
                                case 3:
                                    break
                                case _:
                                    view.get_value_error_message()
                                    continue
                            data.db_save(file_path)
                # Student account.
                case 2:
                    while True:
                        try:
                            student_choice = view.get_student_menu()
                        except ValueError:
                            view.get_value_error_message()
                            continue
                        else:
                            match student_choice:
                                case 1:
                                    student.get_rating()
                                case 2:
                                    break
                                case _:
                                    view.get_value_error_message()
                                    continue
                # Exit.
                case 3:
                    print('\nThank you for using the school database!')
                    break
                # Typo.
                case _:
                    view.get_value_error_message()
                    continue
