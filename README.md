# Student Grade \& Attendance Tracker

## Project Information

**Student name:** Yelnur Akhmetzhan  
**Group:** SE-2504  
**Project title:** Student Grade \& Attendance Tracker

## Project Description

Student Grade \& Attendance Tracker is a simple Python console application for managing student academic records. The program allows the user to add students, edit student information, delete students, search students, add grades, mark attendance, calculate average grades, and find students with low attendance or low average grades.

The project follows the approved proposal and uses the main Python concepts covered during the course.

## Main Features

* Add new students
* Edit student names
* Delete students
* Search students by name or ID
* Add grades for subjects
* Mark attendance as present or absent
* Calculate average grade
* Calculate attendance percentage
* Show students with low average grade
* Show students with low attendance
* Save data to a JSON file
* Load data from a JSON file
* Log user actions using a custom decorator

## Technologies Used

* Python
* Lists
* Dictionaries
* Sets
* Object-Oriented Programming
* Classes and objects
* Functions and methods
* JSON module
* OS module
* Datetime module
* Custom decorators
* Modular project structure

## Project Structure

```text
Student\\\_Grade\\\_Attendance\\\_Tracker/
│
├── main.py
├── models/
│   ├── \\\_\\\_init\\\_\\\_.py
│   └── student.py
├── services/
│   ├── \\\_\\\_init\\\_\\\_.py
│   └── tracker.py
├── utils/
│   ├── \\\_\\\_init\\\_\\\_.py
│   ├── decorators.py
│   └── file\\\_handler.py
├── data/
│   └── students.json
├── logs/
│   └── actions.log
├── diagrams.md
├── defense\\\_script.md
├── README.md
└── requirements.txt
```

## How to Run the Project

1. Open the project folder in VS Code or another code editor.
2. Open the terminal in the project folder.
3. Run this command:

```bash
python main.py
```

If `python` does not work, use:

```bash
python3 main.py
```

## Example Demo Flow

During the live demonstration, use this order:

1. Run `python main.py`
2. Choose option `1` and add a student
3. Choose option `5` and add a grade
4. Choose option `6` and mark attendance
5. Choose option `7` and show all students
6. Choose option `8` and show low average students
7. Choose option `9` and show low attendance students
8. Choose option `11` and save data
9. Open `data/students.json` to show saved data
10. Open `logs/actions.log` to show decorator logging

## Where Course Concepts Are Used

### Object-Oriented Programming

The project uses OOP through the `Student` class and the `Tracker` class.

### Lists

The `Tracker` class stores all student objects in a list called `students`.

### Dictionaries

Each student stores grades and attendance in dictionaries.

### Sets

The project uses a set to collect unique subject names.

### File Handling

The program saves and loads data using the JSON file `data/students.json`.

### External Modules

The project uses built-in Python modules: `json`, `os`, and `datetime`.

### Decorators

The custom decorator `log\\\_action` records important user actions in `logs/actions.log`.



\## Final Project Notes



This project was created as a final project for Introduction to Programming 2.  

It demonstrates object-oriented programming, file handling, data structures, decorators, and modular project organization.



\## Main Python Concepts Used



\- Classes and objects

\- Lists, dictionaries, and sets

\- JSON file handling

\- Custom decorators

\- External modules

\- Modular structure

