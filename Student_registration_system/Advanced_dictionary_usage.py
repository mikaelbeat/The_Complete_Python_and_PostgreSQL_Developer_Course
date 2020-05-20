
student_list = [

def create_student():
    student = input(f"Enter the name of the student: ")
    student_data = {"name": student, "marks": [20, 30]}
    student_list.append(student_data)
    return student_data

def add_course_marks(student, mark):
    student["marks"].append(mark)

def calculate_average_mark(student):
    marks_added = len(student["marks"])
    sum_of_marks = sum(student["marks"])
    if marks_added == 0:
        return 0
    return sum_of_marks / marks_added

def student_details(student):
    name = student["name"]
    marks = student["marks"]
    average = calculate_average_mark(student)
    print(f"Student {name} has marks {marks}. Average is {average}.")

def print_students():
    for student in student_list:
        student_details(student)


student = create_student()
add_course_marks(student, 10)

print(student)
print(calculate_average_mark(student))

#student_details(student)

print_students()
