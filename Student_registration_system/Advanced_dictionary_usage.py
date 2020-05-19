
""" demo = {"name": "Jose",
            "marks": [70, 50, 80, 44, 99],
            "exams":{
                "final": 70,
                "midterm": 50
            }}

print(demo["exams"]["final"]) """


def create_student():
    student = input(f"Enter the name of the student: ")
    student_data = {"name": student, "marks": [20, 30]}
    return student_data

student = create_student()


def add_course_marks(student, mark):
    student["marks"].append(mark)

add_course_marks(student, 10)

print(student)


def calculate_average_mark(student):
    marks_added = len(student["marks"])
    sum_of_marks = sum(student["marks"])
    if marks_added == 0:
        return 0
    return sum_of_marks / marks_added

print(calculate_average_mark(student))


def student_details(student):
    print(student["name"])