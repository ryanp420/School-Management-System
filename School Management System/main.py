import school
from sys import exit


def main():

    choice = 1

    while choice != 0:

        #! Teacher
        user_choice = eval(input("1. Teacher , 2. Student \n"))
        if user_choice == 1:

            #! Teacher Information
            first_name = input("Enter your first name: \n")
            last_name = input("Enter your last name: \n")
            teacher_course1 = input("Enter name of course \n")
            teacher1 = school.Teacher(first_name, last_name, teacher_course1)

            #! Teacher Class Information
            print("Enter course information: \n")
            num_students = eval(input("# Students: "))
            course1 = school.Course(teacher_course1, num_students)

            #! Adding Students
            count = 0

            while count < num_students:
                add_students_names = input("Enter student: \n")
                course1.add_student(add_students_names)
                count += 1

            sum = 0
            add_student_grades = eval(input("Enter # total grades:"))
            for student in course1.students_list:
                print(student)
                grade = eval(input("Grade: "))
                course1.grades.append(grade)
                sum = sum + grade

            class_avg = sum / len(course1.students_list)
            print(course1.students_list)
            print("Grades in class: ", course1.grades)
            print("Class Grade Average = ", class_avg)

            #! Calculating Class

            with open("teacherfile.txt", "a") as teacher_report:
                teacher_report.write(
                    "Instructor:" + first_name + ", " + last_name + "\n"
                )
                teacher_report.write("Course: " + teacher_course1 + "\n")
                teacher_report.write("# Students:" + str(num_students) + "\n")
                teacher_report.write(
                    "Student List: " + str(course1.students_list) + "\n"
                )

                teacher_report.write("Grades: " + str(course1.grades) + "\n")
                teacher_report.write("Class Average = " + str(class_avg) + "\n")
                teacher_report.write("\n")
                teacher_report.write("\n")

        #! STUDENT!
        elif user_choice == 2:
            #! Creating Student Object
            first_name = input("Enter your first name: \n")
            last_name = input("Enter your last name: \n")
            person1 = school.Student(first_name, last_name)

            #! Storing Student Information
            number_of_classes = eval(input("# of Courses: "))
            count = 0
            while count < number_of_classes:
                course_names = person1.enter_course()
                count += 1

            #! Student Courses and Grades
            course = person1.course
            course_list = person1.get_course_list()
            gpa = person1.get_grade_avg()

            print("Grades: ", person1.grades_list)
            print("Grade Average: ", gpa)

            with open("studentfile.txt", "a") as student_report:
                student_report.write(first_name + ", " + last_name + "\n")
                student_report.write("Course List:" + str(course_list) + "\n")
                student_report.write("Grade List: " + str(person1.grades_list) + "\n")
                student_report.write("Grade Average: " + str(gpa) + "\n")
                student_report.write("\n")
        else:
            print("Invalid Input")
            exit()

        choice = eval(input("Enter 1 to continue, or 0 to quit: \n"))


if __name__ == "__main__":
    main()


# afterword:
# program could use polishing:
# cleaner main()
# move most of the teacher and student functions into a seperate file and only call methods
