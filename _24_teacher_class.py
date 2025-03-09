class Teacher:
    def __init__(self, name, subject, years_of_experience):
        self.name = name
        self.subject = subject
        self.years_of_experience = years_of_experience
        self.assigned = False

class Classroom:
    def __init__(self, class_name, capacity):
        self.class_name = class_name
        self.capacity = capacity
        self.teacher = None

    def assign_teacher(self, teacher):
        if not teacher.assigned:
            self.teacher = teacher
            teacher.assigned = True
            print(f"{teacher} has already been assigned to {self.class_name}")

        else:
            print(f"{teacher} has already been assigned to {self.class_name}")

    def display_classroom_info(self):
        if self.teacher:
            teacher_info = f"Teacher: {self.teacher.name} (Subject: {self.teacher.subject}, Experience: {self.teacher.years_of_experience} years)"

        else:
            teacher_info = "No teacher assigned"
        print(f"Classroom Name: {self.class_name}\nCapacity: {self.capacity}\n{teacher_info}")


teacher1 = Teacher('Mr. John', 'Math', 10)
teacher2 = Teacher('Ms. Sarah', 'Science', 8)

classroom1 = Classroom('Physical', 85)
classroom2 = Classroom('Biological', 77)

classroom1.assign_teacher(teacher1)
classroom2.assign_teacher(teacher2)
classroom2.assign_teacher(teacher1)

classroom1.display_classroom_info()
classroom2.display_classroom_info()
