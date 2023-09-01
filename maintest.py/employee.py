class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Position: {self.position}")
