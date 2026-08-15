"""
manager.py
Manager subclass of Employee.

Demonstrates: Inheritance, Method Overriding, Polymorphism
"""

from employee import Employee


class Manager(Employee):
    MANAGEMENT_ALLOWANCE = 8000.0  # flat allowance, adjust as needed

    def __init__(self, employee_id, name, age, email, phone, department,
                 basic_salary, team_size):
        super().__init__(employee_id, name, age, email, phone, department, basic_salary)
        self.team_size = team_size

        # Larger teams get a bigger allowance
        self.management_allowance = self.MANAGEMENT_ALLOWANCE + (self.team_size * 200)

    def manage_team(self):
        print(f"{self.name} is managing a team of {self.team_size} people.")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a team meeting.")

    def calculate_salary(self):
        """Basic Salary + Management Allowance + Bonus"""
        return self.get_salary() + self.management_allowance + self.get_bonus()

    def display_details(self):
        super().display_details()
        print(f"Team Size            : {self.team_size}")
        print(f"Management Allowance : {self.management_allowance:.2f}")
        print("-" * 50)
