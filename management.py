"""
management.py
EmployeeManagementSystem class.

Demonstrates: Composition (contains Employee objects), Polymorphism
(calls calculate_salary() on each employee without checking its class)
"""

from developer import Developer
from manager import Manager
from hr import HR


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []  # list of Employee objects (Developer/Manager/HR)

    # ---------- Add ----------
    def add_employee(self, employee):
        if self.find_employee_by_id(employee.employee_id) is not None:
            print(f"Employee ID {employee.employee_id} already exists. Add rejected.")
            return False
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added successfully.")
        return True

    # ---------- Display ----------
    def display_employees(self):
        if not self.employees:
            print("No employees found in the system.")
            return
        print(f"\nTotal Employees: {len(self.employees)}")
        for emp in self.employees:
            emp.display_details()

    # ---------- Search ----------
    def find_employee_by_id(self, employee_id):
        for emp in self.employees:
            if str(emp.employee_id) == str(employee_id):
                return emp
        return None

    def search_employee(self, keyword):
        """Search by employee ID, name, or department (case-insensitive substring match)."""
        keyword = str(keyword).strip().lower()
        results = [
            emp for emp in self.employees
            if keyword == str(emp.employee_id).lower()
            or keyword in emp.name.lower()
            or keyword in emp.department.lower()
        ]

        if not results:
            print(f"No employees found matching '{keyword}'.")
            return []

        print(f"\nFound {len(results)} matching employee(s):")
        for emp in results:
            emp.display_details()
        return results

    # ---------- Update ----------
    def update_employee(self, employee_id, **kwargs):
        emp = self.find_employee_by_id(employee_id)
        if emp is None:
            print(f"No employee found with ID {employee_id}.")
            return False
        emp.update_details(**kwargs)
        return True

    # ---------- Delete ----------
    def delete_employee(self, employee_id):
        emp = self.find_employee_by_id(employee_id)
        if emp is None:
            print(f"No employee found with ID {employee_id}.")
            return False
        self.employees.remove(emp)
        print(f"Employee ID {employee_id} ({emp.name}) deleted successfully.")
        return True

    # ---------- Attendance ----------
    def mark_attendance(self, employee_id, date, status):
        emp = self.find_employee_by_id(employee_id)
        if emp is None:
            print(f"No employee found with ID {employee_id}.")
            return False
        return emp.mark_attendance(date, status)

    # ---------- Payroll (Polymorphism in action) ----------
    def calculate_payroll(self, employee_id=None):
        """
        If employee_id is given, calculate salary for just that employee.
        Otherwise, calculate and print salary for every employee.
        The system never checks each employee's class -- calculate_salary()
        is polymorphic and each subclass provides its own implementation.
        """
        if employee_id is not None:
            emp = self.find_employee_by_id(employee_id)
            if emp is None:
                print(f"No employee found with ID {employee_id}.")
                return None
            salary = emp.calculate_salary()
            print(f"{emp.name} ({emp.__class__.__name__}) -> Final Salary: {salary:.2f}")
            return salary

        if not self.employees:
            print("No employees found in the system.")
            return {}

        payroll = {}
        print("\n--- Payroll Summary ---")
        for emp in self.employees:
            salary = emp.calculate_salary()
            payroll[emp.employee_id] = salary
            print(f"{emp.employee_id} | {emp.name:<20} | {emp.__class__.__name__:<10} | {salary:.2f}")
        return payroll

    # ---------- Bonus ----------
    def give_bonus(self, employee_id, amount):
        emp = self.find_employee_by_id(employee_id)
        if emp is None:
            print(f"No employee found with ID {employee_id}.")
            return False
        return emp.give_bonus(amount)

    # ---------- Report ----------
    def generate_report(self, employee_id=None):
        """Display a complete employee summary for one employee, or all employees."""
        if employee_id is not None:
            emp = self.find_employee_by_id(employee_id)
            if emp is None:
                print(f"No employee found with ID {employee_id}.")
                return
            emp.display_details()
            return

        self.display_employees()