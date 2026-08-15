Employee Management System

A console-based Employee Management System built with Python and Object-Oriented Programming (OOP).

This project allows users to manage different types of employees such as Developers, Managers, and HRs, while demonstrating important OOP concepts like Encapsulation, Inheritance, Polymorphism, Method Overriding, and Composition.

🚀 Features
Add new employees
Display all employees
Search employees by ID, name, or department
Update employee details
Delete employees
Mark employee attendance
Calculate attendance percentage
Calculate role-based salary
Give bonuses to employees
Generate employee reports
Prevent duplicate employee IDs
Validate salary and bonus values
Console-based interactive menu

👨‍💻 Employee Roles

Developer
Programming language
Experience
Technical allowance
Role-specific salary calculation

Manager

Team size
Management allowance
Team management
Role-specific salary calculation

HR

Employees handled
HR allowance
Recruitment functionality
Role-specific salary calculation

🧠 OOP Concepts Used

Concept	Implementation
Class & Object	Employee, Developer, Manager, HR
Encapsulation	Private __salary attribute
Getter & Setter	get_salary() and set_salary()
Inheritance	Developer, Manager and HR inherit from Employee
Method Overriding	Role-specific calculate_salary() and display_details()
Polymorphism	emp.calculate_salary()
Composition	Management system contains employee objects
Constructor	__init__()
super()	Calling the parent Employee constructor/methods

📂 Project Structure
employee-management-system/
│
├── employee.py
├── developer.py
├── manager.py
├── hr.py
├── management.py
└── main.py

File Description
employee.py — Base Employee class containing common employee information, salary, bonus, attendance and update functionality.
developer.py — Developer subclass with programming language, experience and technical allowance.
manager.py — Manager subclass with team size and management allowance.
hr.py — HR subclass with employees handled and HR allowance.
management.py — Handles employee management operations such as add, search, update, delete, attendance, payroll and reports.
main.py — Console entry point containing the interactive menu.

⚙️ How to Run

Make sure Python is installed on your system.

Clone the repository:

git clone <your-repository-url>

Go to the project folder:

cd employee-management-system

Run the application:

python main.py
🖥️ Main Menu
========================================
EMPLOYEE MANAGEMENT SYSTEM
========================================
1. Add Employee
2. Display All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Mark Attendance
7. Calculate Salary
8. Give Bonus
9. Employee Report
10. Exit
💰 Salary Calculation

Salary calculation is different for each employee role.

Developer:
Basic Salary + Technical Allowance + Bonus


Manager:
Basic Salary + Management Allowance + Bonus


HR:
Basic Salary + HR Allowance + Bonus

This demonstrates Polymorphism, because the same calculate_salary() method behaves differently depending on the employee object.

🛠️ Technologies Used
Python 3
Object-Oriented Programming
Lists
Dictionaries
Functions and Methods
Exception Handling
Console Input/Output
🎯 Learning Objectives

This project was created to practice and demonstrate:

Python OOP fundamentals
Designing classes and objects
Inheritance and reusable code
Encapsulation and data protection
Polymorphism and method overriding
Managing collections of objects
Building a menu-driven console application

👤 Author
Vedik Gurjar
