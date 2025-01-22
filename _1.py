class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        self.tasks = []


    def assign_task(self, task):
        if task in self.tasks:
            print(f"The task '{task}' has already been assigned to {self.name} ")

        else:
            self.tasks.append(task)
            print(f"The task '{task}' has been assigned to {self.name}")

    def display_emploeyee_info(self):
        task_list = self.tasks if self.tasks else "No tasks assigned."
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nEmployee Id: {self.employee_id}\nDepartment: {self.department}\nTasks: {task_list}")


emp1 = Employee('John', 21, 'Male', 'E121', 'Development')
emp2 = Employee('Ruth', 20, 'Female', 'E002', 'Testing')

emp1.assign_task('Debugging')
emp1.assign_task('Model Development')
emp1.assign_task('Testing')

print('-'*60)
emp1.display_emploeyee_info()
print('-'*60)
emp2.display_emploeyee_info()