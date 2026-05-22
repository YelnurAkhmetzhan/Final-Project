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

The architecture diagram shows the main structure of the project.  
The user interacts with the menu in `main.py`. The menu calls the `Tracker` service, which manages students, grades, attendance, file handling, and logging.

---

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

The UML class diagram shows the two main classes of the project.  
The `Student` class stores information about one student, while the `Tracker` class manages all students and the main project operations.

---

## 3. Program Flowchart

```mermaid
flowchart LR
    A([Start Program]) --> B[Load Data from JSON]
    B --> C[Show Main Menu]
    C --> D{User Selects Option}

    D --> E[Manage Students]
    E --> E1[Add Student]
    E --> E2[Edit Student]
    E --> E3[Delete Student]
    E --> E4[Search Student]
    E1 --> C
    E2 --> C
    E3 --> C
    E4 --> C

    D --> F[Add Grade]
    F --> F1[Select Student]
    F1 --> F2[Enter Subject and Grade]
    F2 --> F3[Update Student Grades]
    F3 --> C

    D --> G[Mark Attendance]
    G --> G1[Select Student]
    G1 --> G2[Enter Attendance Status]
    G2 --> G3[Update Attendance Records]
    G3 --> C

    D --> H[Show Reports]
    H --> H1[Calculate Average Grade]
    H --> H2[Show Low Grade Students]
    H --> H3[Show Low Attendance Students]
    H1 --> C
    H2 --> C
    H3 --> C

    D --> I[Save Data]
    I --> I1[Write Data to JSON File]
    I1 --> C

    D --> J[Exit]
    J --> K[Save Data Before Closing]
    K --> L([End Program])
```

The flowchart shows the main execution process of the program.  
The application starts by loading saved data from a JSON file. Then, the main menu is displayed, and the user selects an action. After completing each action, the program returns to the main menu. When the user chooses to exit, the data is saved before the program closes.