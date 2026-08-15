class Employee:

    def __init__(self, employee_id, name, age, email, phone, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.department = department
        self.__salary = salary
        self.bonus = 0
        self.attendence = {}

    # ---------- Display Details ----------
    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Department:", self.department)
        print("Salary:", self.__salary)
        print("Bonus:", self.bonus)

    # ---------- Salary ----------
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print("Salary updated successfully.")
            return True
        else:
            print("Salary cannot be negative.")
            return False

    # ---------- Bonus ----------
    def get_bonus(self):
        return self.bonus

    def give_bonus(self, amount):
        if amount >= 0:
            self.bonus += amount
            print("Bonus added successfully.")
            return True
        else:
            print("Bonus cannot be negative.")
            return False

    # ---------- Attendance ----------
    def mark_attendance(self, date, status):
        status = status.capitalize()

        if status in ["Present", "Absent"]:
            self.attendence[date] = status
            print("Attendance marked successfully.")
            return True
        else:
            print("Status must be Present or Absent.")
            return False

    def get_attendance_percentage(self):
        if not self.attendence:
            return 0

        present_days = sum(
            1
            for status in self.attendence.values()
            if status == "Present"
        )

        return (present_days / len(self.attendence)) * 100

    # ---------- Update Details ----------
    def update_details(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        print("Employee details updated successfully.")
