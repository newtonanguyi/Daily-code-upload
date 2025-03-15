class Course:
    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits

class Instructor:
    def __init__(self, name):
        self.name = name
        self.courses_taught = []

    def assign_course(self, course):
        if course in self.courses_taught:
            print(f"Course '{course}' is already assigned.")

        else:
            self.courses_taught.append(course)

    def display_instructor_info(self):
        print(f"Instructor Name: {self.name}")
        print(f"Courses Taught: ")
        for course in self.courses_taught:
            print(f"- {course.course_name} ({course.course_code}), Credits: {course.credits}")


course1 = Course('Computer Science', 'BSCS', 5)
course2 = Course('Civil Engineering', 'BSCEE', 3)
course3 = Course('Business Administration', 'BBA', 4)

ins1 = Instructor('Dr. John')

ins1.assign_course(course1)
ins1.assign_course(course3)

ins1.display_instructor_info()

