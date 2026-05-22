from models.student import Student
from utils.decorators import log_action
from utils.file_handler import save_students, load_students


class Tracker:
    def __init__(self):
        self.students = []

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    @log_action
    def add_student(self, student_id, name):
        existing_student = self.find_student_by_id(student_id)

        if existing_student is not None:
            return False

        student = Student(student_id, name)
        self.students.append(student)
        return True

    @log_action
    def edit_student(self, student_id, new_name):
        student = self.find_student_by_id(student_id)

        if student is None:
            return False

        student.name = new_name
        return True

    @log_action
    def delete_student(self, student_id):
        student = self.find_student_by_id(student_id)

        if student is None:
            return False

        self.students.remove(student)
        return True

    def search_student(self, keyword):
        results = []

        for student in self.students:
            if keyword.lower() in student.name.lower() or keyword == student.student_id:
                results.append(student)

        return results

    @log_action
    def add_grade(self, student_id, subject, grade):
        student = self.find_student_by_id(student_id)

        if student is None:
            return False

        student.add_grade(subject, grade)
        return True

    @log_action
    def mark_attendance(self, student_id, date, status):
        student = self.find_student_by_id(student_id)

        if student is None:
            return False

        student.mark_attendance(date, status)
        return True

    def get_low_average_students(self, limit):
        low_students = []

        for student in self.students:
            if student.calculate_average() < limit:
                low_students.append(student)

        return low_students

    def get_low_attendance_students(self, limit):
        low_students = []

        for student in self.students:
            if student.calculate_attendance_percentage() < limit:
                low_students.append(student)

        return low_students

    def get_all_subjects(self):
        subjects = set()

        for student in self.students:
            student_subjects = student.get_subjects()
            for subject in student_subjects:
                subjects.add(subject)

        return subjects

    @log_action
    def save_data(self):
        save_students(self.students)

    @log_action
    def load_data(self):
        self.students = load_students()

    def show_all_students(self):
        return self.students
