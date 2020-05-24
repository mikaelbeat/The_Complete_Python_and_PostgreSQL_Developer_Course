
student_list = []

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def calculate_average_mark(self):
        marks_added = len(self.marks)
        sum_of_marks = sum(self.marks)
        if marks_added == 0:
            return 0
        return sum_of_marks / marks_added


def create_student():
    name = input(f"\nEnter the name of the student: ")
    student_data = Student(name)
    return student_data

def add_course_marks(student, mark):
    student.marks.append(mark)

def student_details(student):
    name = student.name
    marks = student.marks
    average = student.calculate_average_mark()
    print(f"Student {name} has marks {marks}. Average is {average}.")

def print_students(students):
    for i, student in enumerate(students):
        print(f"\nID - {i}")
        student_details(student)

def menu():
    print("\n*** STUDENT REGISTERATION ***\n")
    print("1 - Add a student.")
    print("2 - Add a mark to a student.")
    print("3 - List all students.")
    print("4 - Quit\n")
    selection = int(input("What would you like to do: "))

    while selection != 4:
        if selection == 1:
            student_list.append(create_student())
        elif selection == 2:
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_course_marks(student, new_mark)
        elif selection == 3:
            print_students(student_list)

        print("\n*** STUDENT RESISTERATION ***\n")
        print("1 - Add a student.")
        print("2 - Add a mark to a student.")
        print("3 - List all students.")
        print("4 - Quit\n")
        selection = int(input("What would you like to do: "))

    print("\nQuitting...")

menu()
