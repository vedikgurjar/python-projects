"""
hr.py
HR subclass of Employee.

Demonstrates: Inheritance, Method Overriding, Polymorphism
"""

from employee import Employee


class HR(Employee):
    HR_ALLOWANCE = 4000.0  # flat allowance, adjust as needed

    def __init__(self, employee_id, name, age, email, phone, department,
                 basic_salary, employees_handled):
        super().__init__(employee_id, name, age, email, phone, department, basic_salary)
        self.employees_handled = employees_handled

        # More employees handled -> slightly higher allowance
        self.hr_allowance = self.HR_ALLOWANCE + (self.employees_handled * 100)

    def recruit_employee(self):
        print(f"{self.name} is recruiting new employees.")

    def calculate_salary(self):
        """Basic Salary + HR Allowance + Bonus"""
        return self.get_salary() + self.hr_allowance + self.get_bonus()

    def display_details(self):
        super().display_details()
        print(f"Employees Handled : {self.employees_handled}")
        print(f"HR Allowance      : {self.hr_allowance:.2f}")
        print("-" * 50)
