from employee import Employee
from customer import Customer

employees = []
customers = []

while True:
    print("\nOptions:")
    print("1. Add a Customer")
    print("2. Add an Employee")
    print("3. Display Customer and Employee Information")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer's name: ")
        loan = float(input("Enter customer's loan amount: "))
        salary = float(input("Enter customer's salary: "))
        customer = Customer(name, loan, salary)
        customers.append(customer)
        print("Customer information added successfully.")

    elif choice == '2':
        name = input("Enter employee's name: ")
        salary = float(input("Enter employee's salary: "))
        position = input("Enter employee's position: ")
        employee = Employee(name, salary, position)
        employees.append(employee)
        print("Employee information added successfully.")

    elif choice == '3':
        print("\nCustomer Information:")
        for customer in customers:
            customer.display_info()
        print("\nEmployee Information:")
        for employee in employees:
            employee.display_info()

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
