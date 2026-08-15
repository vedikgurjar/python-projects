"""
main.py
Console entry point for the Employee Management System.
"""

from management import EmployeeManagementSystem
from developer import Developer
from manager import Manager
from hr import HR


def print_menu():
    print("\n" + "=" * 40)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Mark Attendance")
    print("7. Calculate Salary")
    print("8. Give Bonus")
    print("9. Employee Report")
    print("10. Exit")


def input_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Try again.")


def input_number(prompt, allow_float=True):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw) if allow_float else int(raw)
        except ValueError:
            print("Please enter a valid number.")


def add_employee_flow(system):
    print("\nSelect role: 1) Developer  2) Manager  3) HR")
    role_choice = input("Enter choice: ").strip()

    employee_id = input_nonempty("Employee ID: ")
    if system.find_employee_by_id(employee_id) is not None:
        print(f"Employee ID {employee_id} already exists.")
        return

    name = input_nonempty("Name: ")
    age = input_number("Age: ", allow_float=False)
    email = input_nonempty("Email: ")
    phone = input_nonempty("Phone: ")
    department = input_nonempty("Department: ")
    basic_salary = input_number("Basic Salary: ")

    if role_choice == "1":
        language = input_nonempty("Programming Language: ")
        experience = input_number("Experience (years): ", allow_float=False)
        emp = Developer(employee_id, name, age, email, phone, department,
                         basic_salary, language, experience)
    elif role_choice == "2":
        team_size = input_number("Team Size: ", allow_float=False)
        emp = Manager(employee_id, name, age, email, phone, department,
                       basic_salary, team_size)
    elif role_choice == "3":
        handled = input_number("Employees Handled: ", allow_float=False)
        emp = HR(employee_id, name, age, email, phone, department,
                 basic_salary, handled)
    else:
        print("Invalid role choice. Employee not added.")
        return

    system.add_employee(emp)


def update_employee_flow(system):
    employee_id = input_nonempty("Employee ID to update: ")
    if system.find_employee_by_id(employee_id) is None:
        print(f"No employee found with ID {employee_id}.")
        return

    print("Leave a field blank to keep it unchanged.")
    fields = {}
    for field, prompt in [
        ("name", "New Name: "),
        ("age", "New Age: "),
        ("email", "New Email: "),
        ("phone", "New Phone: "),
        ("department", "New Department: "),
    ]:
        value = input(prompt).strip()
        if value:
            fields[field] = value

    system.update_employee(employee_id, **fields)

    change_salary = input("Update salary too? (y/n): ").strip().lower()
    if change_salary == "y":
        emp = system.find_employee_by_id(employee_id)
        new_salary = input_number("New Basic Salary: ")
        emp.set_salary(new_salary)


def main():
    system = EmployeeManagementSystem()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee_flow(system)

        elif choice == "2":
            system.display_employees()

        elif choice == "3":
            keyword = input_nonempty("Search by ID, name, or department: ")
            system.search_employee(keyword)

        elif choice == "4":
            update_employee_flow(system)

        elif choice == "5":
            employee_id = input_nonempty("Employee ID to delete: ")
            system.delete_employee(employee_id)

        elif choice == "6":
            employee_id = input_nonempty("Employee ID: ")
            date = input_nonempty("Date (YYYY-MM-DD): ")
            status = input_nonempty("Status (Present/Absent): ")
            system.mark_attendance(employee_id, date, status)

        elif choice == "7":
            employee_id = input("Employee ID (blank = all employees): ").strip()
            system.calculate_payroll(employee_id if employee_id else None)

        elif choice == "8":
            employee_id = input_nonempty("Employee ID: ")
            amount = input_number("Bonus Amount: ")
            system.give_bonus(employee_id, amount)

        elif choice == "9":
            employee_id = input("Employee ID (blank = all employees): ").strip()
            system.generate_report(employee_id if employee_id else None)

        elif choice == "10":
            print("Exiting Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1-10.")


if __name__ == "__main__":
    main()
