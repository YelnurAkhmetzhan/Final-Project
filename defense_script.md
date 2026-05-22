# Defense Script

## Short Introduction

Good afternoon. My name is Yelnur Akhmetzhan, and today I will present my final project called Student Grade & Attendance Tracker. This project is a Python console application that helps manage student academic records. The system allows the user to add students, record grades, track attendance, calculate average scores, and save all information in files.

## Project Goal

The main goal of this project is to make student progress tracking simple and organized. A teacher or student can use the program to store student information, check academic performance, and find students who have low grades or low attendance.

## Main Features

The project has several main features. First, the user can add, edit, delete, and search students. Second, the user can add grades for different subjects. Third, the user can mark attendance as present or absent. The program can also calculate the average grade and attendance percentage for each student. Finally, the program saves and loads data using a JSON file.

## Technical Requirements

This project uses the main Python concepts from the course. I used Object-Oriented Programming by creating two main classes: Student and Tracker. The Student class stores information about one student, such as ID, name, grades, and attendance. The Tracker class manages all students and contains the main project logic.

I used a list to store all students. I used dictionaries to store grades and attendance for each student. I also used a set to collect unique subject names. For file handling, I used the JSON module to save and load student data. I also used the OS module to create folders and the Datetime module to write the time of each logged action.

## Decorator Explanation

The project also uses a custom decorator called log_action. This decorator is used to log important user actions. For example, when the user adds a student, adds a grade, marks attendance, saves data, or loads data, the decorator writes this action into the actions.log file. This makes the project more organized and shows how decorators can add extra behavior to functions.

## Project Structure

The project has a modular structure. The main.py file contains the menu and controls the program execution. The models folder contains the Student class. The services folder contains the Tracker class. The utils folder contains helper files for file handling and decorators. The data folder stores students.json, and the logs folder stores actions.log.

## Diagrams

The presentation includes three diagrams. The architecture diagram shows how the user, menu, tracker, student model, JSON file, and log file are connected. The UML class diagram shows the Student and Tracker classes and their methods. The flowchart shows the execution process of the program from starting the application to choosing menu options and saving data.

## Live Demonstration Plan

During the live demo, I will run the project using python main.py. Then I will add a student, add a grade, mark attendance, and show all students. After that, I will save the data and open the students.json file to show that the information was saved. I will also open the actions.log file to show that the decorator logged the actions.

## Challenges and Solutions

One challenge was organizing the project into multiple files. I solved this by separating the code into models, services, and utilities. Another challenge was saving objects into a JSON file because Python objects cannot be saved directly. I solved this by converting Student objects into dictionaries before saving them.

## Conclusion

In conclusion, the project successfully implements the planned features from the proposal. It uses OOP, data structures, file handling, external modules, decorators, and a clean project structure. This project helped me practice how to build a complete Python application using the concepts learned during the course.
