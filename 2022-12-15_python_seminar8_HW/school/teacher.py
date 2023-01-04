import data


def add_student():
    """Add a new student."""
    while True:
        student_data = input("Enter the student's data (last name, first name, class separated by a space): ")
        if student_data == '':
            print('The value cannot be empty, please try again...')
            continue
        else:
            student_data = student_data.split(' ')
            data.students[student_data[0]] = student_data[1:], {}
            print('\nEntry added successfully!')
            break


def add_rating():
    """Add a grade for the subject to the student."""
    last_name = input("Enter student's last name: ")
    if data.students.get(last_name) is None:
        print(f'\nStudent with last name "{last_name}" not found!')
    else:
        while True:
            lesson = input('Enter the name of the lesson: ')
            if lesson == '':
                print('The value cannot be empty, please try again...')
                continue
            else:
                break
        while True:
            grade = input('Enter the grade(s) separated by a space: ').split(' ')
            try:
                list(map(int, grade))
            except ValueError:
                print('Sorry, invalid input, please try again...')
                continue
            else:
                if lesson in data.students[last_name][1]:
                    data.students[last_name][1][lesson].extend(grade)
                else:
                    data.students[last_name][1][lesson] = grade
                print('\nEntry added successfully!')
                break
