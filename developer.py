"""
developer.py
Developer subclass of Employee.

Demonstrates: Inheritance, Method Overriding, Polymorphism
"""

from employee import Employee


class Developer(Employee):
    TECHNICAL_ALLOWANCE = 5000.0  # flat allowance, adjust as needed

    def __init__(self, employee_id, name, age, email, phone, department,
                 basic_salary, programming_language, experience):
        super().__init__(employee_id, name, age, email, phone, department, basic_salary)
        self.programming_language = programming_language
        self.experience = experience  # years

        # Experience-based bump to the technical allowance
        self.technical_allowance = self.TECHNICAL_ALLOWANCE + (self.experience * 500)

    def write_code(self):
        print(f"{self.name} is writing {self.programming_language} code.")

    def calculate_salary(self):
        """Basic Salary + Technical Allowance + Bonus"""
        return self.get_salary() + self.technical_allowance + self.get_bonus()

    def display_details(self):
        super().display_details()
        print(f"Programming Language : {self.programming_language}")
        print(f"Experience            : {self.experience} yrs")
        print(f"Technical Allowance   : {self.technical_allowance:.2f}")
        print("-" * 50)
