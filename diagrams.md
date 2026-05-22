# Diagrams for Presentation

## 1. Architecture Diagram

```mermaid
flowchart TD
    A[User] --> B[main.py Menu]
    B --> C[Tracker Service]
    C --> D[Student Model]
    C --> E[File Handler]
    C --> F[Logging Decorator]
    E --> G[students.json]
    F --> H[actions.log]
```

## 2. UML Class Diagram

```mermaid
classDiagram
    class Student {
        +student_id
        +name
        +grades
        +attendance
        +add_grade(subject, grade)
        +mark_attendance(date, status)
        +calculate_average()
        +calculate_attendance_percentage()
        +get_subjects()
        +to_dictionary()
        +from_dictionary(data)
    }

    class Tracker {
        +students
        +add_student(student_id, name)
        +edit_student(student_id, new_name)
        +delete_student(student_id)
        +search_student(keyword)
        +add_grade(student_id, subject, grade)
        +mark_attendance(student_id, date, status)
        +get_low_average_students(limit)
        +get_low_attendance_students(limit)
        +get_all_subjects()
        +save_data()
        +load_data()
    }

    Tracker "1" --> "many" Student
```

## 3. Program Flowchart

flowchart LR
    A([Start Program]) --> B[Load Data from JSON]
    B --> C[Show Main Menu]
    C --> D{User Selects Option}

    D --> E[Manage Students]
    E --> E1[Add / Edit / Delete / Search Student]
    E1 --> C

    D --> F[Add Grade]
    F --> F1[Update Student Grades]
    F1 --> C

    D --> G[Mark Attendance]
    G --> G1[Update Attendance Records]
    G1 --> C

    D --> H[Show Reports]
    H --> H1[Average Grade / Low Attendance / Low Grade]
    H1 --> C

    D --> I[Save Data]
    I --> I1[Write Data to JSON File]
    I1 --> C

    D --> J[Exit]
    J --> K[Save Data Before Closing]
    K --> L([End Program])