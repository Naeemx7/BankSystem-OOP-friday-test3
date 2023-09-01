class Customer:
    def __init__(self, name, loan, salary):
        self.name = name
        self.loan = loan
        self.salary = salary

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Loan: ${self.loan}")
        print(f"Salary: ${self.salary}")
