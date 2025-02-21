class Company:
    def __init__(self, company_name, industry, total_employees):
        self.company_name = company_name
        self.industry = industry
        self.total_employees = total_employees

class Department:
    def __init__(self, department_name, manager_name, employee_count):
        self.department_name = department_name
        self.manager_name = manager_name
        self.employee_count = employee_count
        self.employees = []

    def add_employee(self, employee_name):
        if employee_name in self.employees:
            print(f"Employee {employee_name} is already a part of the department.")

        else:
            self.employees.append(employee_name)
            print(f"Employee {employee_name} has been added to the department.")

    def remove_employee(self, employee_name):
        if employee_name in self.employees:
            self.employees.remove(employee_name)
            print(f"Employee {employee_name} has been removed from the department.")

        else:
            print(f"Cannot remove employee {employee_name} because he/she is not part of the department.")

    def display_department_info(self):
        print("-"*60)
        print(f"Department Name: {self.department_name}\nManager Name: {self.manager_name}\nEmployee Count: {self.employee_count}")
        print("-" * 60)
        print("Employees:")
        for emp in self.employees:
            print(emp)



company = Company('Flix-Tech', 'Technology', 3500)

department = Department('Product Development', 'John Dutton', 300)
department.add_employee('Zack Dee')
department.add_employee('Jack Lee')
department.add_employee('Bruce Selt')

# department.remove_employee('Zack Dee')
department.remove_employee('Jack Chan')

department.display_department_info()

