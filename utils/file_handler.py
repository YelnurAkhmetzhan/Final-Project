import json
import os
from models.student import Student

DATA_FILE = "data/students.json"


def save_students(students):
    os.makedirs("data", exist_ok=True)

    data = []
    for student in students:
        data.append(student.to_dictionary())

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    students = []
    for item in data:
        students.append(Student.from_dictionary(item))

    return students
