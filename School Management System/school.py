class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.course = ()
        self.grades_list = []
        self.course_list = []

    def get_name(self):
        print(f"{self.first_name} {self.last_name}")

    def enter_course(self):
        self.course = str(input("Enter course name: \n"))
        self.course_list.append(self.course)

    def get_course(self):
        return self.course

    def get_course_list(self):
        return self.course_list

    def get_grade_avg(self):
        value = 0
        amount_grades = int(input("Enter amount of grades: "))
        for i in range(amount_grades):
            grade = int(input("Enter grade: "))
            value = value + grade
            self.grades_list.append(grade)
            grade_avg = value / len(self.grades_list)
        return grade_avg
        # return print("Grade average = ", grade_avg)


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.grades = []
        self.students_list = []

    def add_student(self, student):
        if len(self.students_list) < self.max_students:
            self.students_list.append(student)
            return True
        return False


class Teacher(Student, Course):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    # def class_avg(self, name_of_course):
    #     self.course_name
    #     self.name_of_course = name_of_course
    #     return self.max_students / Student.grade
