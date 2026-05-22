class Student:
    def __init__(self, student_id, name, grades=None, attendance=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades is not None else {}
        self.attendance = attendance if attendance is not None else {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def mark_attendance(self, date, status):
        self.attendance[date] = status

    def calculate_average(self):
        all_grades = []

        for subject in self.grades:
            for grade in self.grades[subject]:
                all_grades.append(grade)

        if len(all_grades) == 0:
            return 0

        return sum(all_grades) / len(all_grades)

    def calculate_attendance_percentage(self):
        total_lessons = len(self.attendance)

        if total_lessons == 0:
            return 0

        present_count = 0
        for date in self.attendance:
            if self.attendance[date] == "present":
                present_count += 1

        return (present_count / total_lessons) * 100

    def get_subjects(self):
        subjects = set()

        for subject in self.grades:
            subjects.add(subject)

        return subjects

    def to_dictionary(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grades": self.grades,
            "attendance": self.attendance
        }

    @staticmethod
    def from_dictionary(data):
        return Student(
            data["student_id"],
            data["name"],
            data.get("grades", {}),
            data.get("attendance", {})
        )

    def __str__(self):
        average = self.calculate_average()
        attendance = self.calculate_attendance_percentage()

        return f"ID: {self.student_id} | Name: {self.name} | Average: {average:.2f} | Attendance: {attendance:.2f}%"
