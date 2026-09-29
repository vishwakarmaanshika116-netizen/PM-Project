import pandas as pd


# ==============================
# Base Class
# ==============================

class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def percentage(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def result(self):
        if all(mark >= 35 for mark in self.marks):
            return "PASS"
        else:
            return "FAIL"

    def student_type(self):
        return "Regular Student"


# ==============================
# Child Class 1
# ==============================

class RegularStudent(Student):

    def student_type(self):
        return "Regular Student"


# ==============================
# Child Class 2
# ==============================

class ScholarStudent(Student):

    def student_type(self):
        return "Scholar Student"


# ==============================
# List to store students
# ==============================

students = []


# Tuple of subjects
subjects = ("Python", "Data Structures", "Mathematics", "AI")


# Set for unique student types
student_types = set()


# ==============================
# Function to add student
# ==============================

def add_student():

    print("\n--- Add Student ---")

    roll_no = int(input("Enter Roll Number: "))

    name = input("Enter Student Name: ")

    age = int(input("Enter Age: "))

    print("\nEnter marks out of 100:")

    marks = []

    for subject in subjects:

        mark = float(input(f"Enter marks in {subject}: "))

        if mark < 0 or mark > 100:
            print("Invalid marks!")
            return

        marks.append(mark)

    print("\n1. Regular Student")
    print("2. Scholar Student")

    choice = input("Enter student type: ")

    if choice == "2":
        student = ScholarStudent(
            roll_no, name, age, marks
        )
    else:
        student = RegularStudent(
            roll_no, name, age, marks
        )

    students.append(student)

    student_types.add(student.student_type())

    print("\nStudent added successfully!")


# ==============================
# Function to display students
# ==============================

def display_students():

    if not students:
        print("\nNo students available.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:

        print("\nRoll No:", student.roll_no)
        print("Name:", student.name)
        print("Age:", student.age)

        print("Marks:", student.marks)

        print("Total:", student.total_marks())

        print("Percentage:",
              round(student.percentage(), 2))

        print("Grade:", student.grade())

        print("Result:", student.result())

        print("Type:", student.student_type())


# ==============================
# Search Student
# ==============================

def search_student():

    roll_no = int(input("\nEnter Roll Number to search: "))

    found = False

    for student in students:

        if student.roll_no == roll_no:

            print("\nStudent Found!")

            print("Name:", student.name)
            print("Age:", student.age)
            print("Percentage:",
                  round(student.percentage(), 2))
            print("Grade:", student.grade())
            print("Result:", student.result())

            found = True
            break

    if not found:
        print("Student not found.")


# ==============================
# Find Topper
# ==============================

def find_topper():

    if not students:
        print("\nNo students available.")
        return

    topper = students[0]

    for student in students:

        if student.percentage() > topper.percentage():
            topper = student

    print("\n========== TOPPER ==========")

    print("Roll No:", topper.roll_no)
    print("Name:", topper.name)
    print("Percentage:",
          round(topper.percentage(), 2))
    print("Grade:", topper.grade())


# ==============================
# Display Passed Students
# ==============================

def display_passed():

    print("\n========== PASSED STUDENTS ==========")

    found = False

    for student in students:

        if student.result() == "PASS":

            print(
                student.roll_no,
                "-",
                student.name,
                "-",
                round(student.percentage(), 2)
            )

            found = True

    if not found:
        print("No passed students.")


# ==============================
# Display Failed Students
# ==============================

def display_failed():

    print("\n========== FAILED STUDENTS ==========")

    found = False

    for student in students:

        if student.result() == "FAIL":

            print(
                student.roll_no,
                "-",
                student.name,
                "-",
                round(student.percentage(), 2)
            )

            found = True

    if not found:
        print("No failed students.")


# ==============================
# Pandas DataFrame
# ==============================

def create_dataframe():

    if not students:
        print("\nNo student data available.")
        return

    data = []

    for student in students:

        data.append({
            "Roll No": student.roll_no,
            "Name": student.name,
            "Age": student.age,
            "Python": student.marks[0],
            "Data Structures": student.marks[1],
            "Mathematics": student.marks[2],
            "AI": student.marks[3],
            "Total": student.total_marks(),
            "Percentage": round(student.percentage(), 2),
            "Grade": student.grade(),
            "Result": student.result(),
            "Type": student.student_type()
        })

    df = pd.DataFrame(data)

    print("\n========== PANDAS DATAFRAME ==========")

    print(df.to_string(index=False))

    print("\nAverage Percentage:",
          round(df["Percentage"].mean(), 2))

    print("Highest Percentage:",
          df["Percentage"].max())

    print("Lowest Percentage:",
          df["Percentage"].min())


# ==============================
# Show Student Types
# ==============================

def show_student_types():

    print("\nUnique Student Types:")

    for student_type in student_types:
        print("-", student_type)


# ==============================
# Main Menu
# ==============================

def main():

    while True:

        print("\n\n================================")
        print(" STUDENT PERFORMANCE SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Find Topper")
        print("5. Display Passed Students")
        print("6. Display Failed Students")
        print("7. Pandas Data Analysis")
        print("8. Show Student Types")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            find_topper()

        elif choice == "5":
            display_passed()

        elif choice == "6":
            display_failed()

        elif choice == "7":
            create_dataframe()

        elif choice == "8":
            show_student_types()

        elif choice == "9":
            print("\nThank you!")
            breakvs

        else:
            print("\nInvalid choice!")

            continue


# ==============================
# Program Execution
# ==============================

if __name__ == "__main__":
    main()