import json
import os

students = {}


def db_load(file_path):
    """Load data from the database."""
    global students
    if os.stat(file_path).st_size == 0:
        students = {}
    else:
        with open(file_path, 'r', encoding='utf8') as file:
            students = json.load(file)


def db_save(file_path):
    """Save the data to the database."""
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(students, file)
