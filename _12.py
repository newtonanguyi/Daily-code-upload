class Teacher:
    def __init__(self, name, subject, years_of_experience):
        self.name = name
        self.subject = subject
        self.years_of_experience = years_of_experience

class Classroom:
    def __init__(self, class_code):
        self.class_code = class_code
        self.student_list = []

    def add_student(self, student_name):
        if student_name not in self.student_list:
            self.student_list.append(student_name)
            print(f"The student {student_name} has been added to the class.")
        else:
            print(f"The student {student_name} is already a member of the class.")


    def remove_student(self, student_name):
        if student_name in self.student_list:
            self.student_list.remove(student_name)
            print(f"The student {student_name} has been removed from the class.")
        else:
            print(f"Cannot remove the student {student_name} becuase he/she is not a member of the class.")

    def display_class_info(self):
        print(f"Class Code: {self.class_code}\nStudents: {self.student_list}")

class1 = Classroom('CS212')

class1.add_student('Jonah')
class1.add_student('Mark')
class1.add_student('Kigozi')
class1.add_student('Ian')
class1.add_student('Timothy')
class1.add_student('Hero')

class1.remove_student('Hero')
class1.remove_student('Jane')

print("-"*60)
class1.display_class_info()