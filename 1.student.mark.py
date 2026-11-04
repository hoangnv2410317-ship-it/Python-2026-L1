
# ==============================
# STUDENT MANAGEMENT SYSTEM
# ==============================

students = []
courses = []
marks = {}


# 1. Input number of students
def input_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nStudent {i + 1}")

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth (DD/MM/YYYY): ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    print("Students added successfully!")


# 2. Input number of courses and course information
def input_courses():
    n = int(input("Enter number of courses: "))

    for i in range(n):
        print(f"\nCourse {i + 1}")

        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")

        course = {
            "id": course_id,
            "name": course_name
        }

        courses.append(course)

    print("Courses added successfully!")


# 3. Select a course and input student marks
def input_marks():
    if not courses or not students:
        print("Please input students and courses first!")
        return

    list_courses()

    course_id = input("\nEnter course ID: ")

    course_exists = False

    for course in courses:
        if course["id"] == course_id:
            course_exists = True
            break

    if not course_exists:
        print("Course not found!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        print(f"\nStudent: {student['name']}")
        score = float(input("Enter mark: "))

        marks[course_id][student["id"]] = score

    print("Marks added successfully!")


# 4. List all courses
def list_courses():
    print("\n========== COURSE LIST ==========")

    for course in courses:
        print(course["id"], "-", course["name"])


# 5. List all students
def list_students():
    print("\n========== STUDENT LIST ==========")

    for student in students:
        print(
            student["id"],
            "-",
            student["name"],
            "-",
            student["dob"]
        )


# 6. Show student marks for a given course
def show_marks():
    if not courses:
        print("No courses available!")
        return

    list_courses()

    course_id = input("\nEnter course ID: ")

    if course_id not in marks:
        print("No marks available for this course!")
        return

    print("\n========== STUDENT MARKS ==========")

    for student in students:
        student_id = student["id"]

        if student_id in marks[course_id]:
            print(
                student["name"],
                ":",
                marks[course_id][student_id]
            )
        else:
            print(student["name"], ": No mark yet")


# 7. Main menu
def main():
    while True:
        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_students()

        elif choice == "2":
            input_courses()

        elif choice == "3":
            input_marks()

        elif choice == "4":
            list_courses()

        elif choice == "5":
            list_students()

        elif choice == "6":
            show_marks()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run program
main()
