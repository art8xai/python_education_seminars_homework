import data


def get_rating():
    """Return grades for each student subject."""
    last_name = input("Enter student's last name: ")
    if data.students.get(last_name) is None:
        print(f'\nStudent with last name "{last_name}" not found!')
    else:
        other_student_data = data.students[last_name]
        print('\nInformation found about the student:')
        print(f'{last_name} {", ".join(other_student_data[0])}')
        print(*[f'{key}: {", ".join(value)}' for key, value in other_student_data[1].items()], sep='\n')
