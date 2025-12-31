students = []

def calculate_average(marks):
    total = 0
    for x in marks:
        total += x
    return total/len(marks)


def add_student(name, marks):
    students.append({
        "name": name,
        "marks": marks,
        "average": calculate_average(marks)
    })


def search_student(name):
    for x in students:
        if x["name"].lower() == name.lower():
            return x
    return None

def class_average():
    total = 0

    if len(students) == 0:
        return 0
    else:
        for x in students:
            total += x["average"]
        return total/len(students)


def top_students():
    if not students:
        return []

    top_avg = students[0]["average"]
    for x in students:
        if x["average"] > top_avg:
            top_avg = x["average"]

    toppers = []
    for x in students:
        if x["average"] == top_avg:
            toppers.append(x)

    return toppers



n = int(input("Enter number of students: "))

for x in range(n):
    name = input(f"Enter name of student {x+1}: ")

    marks = []
    for y in range(5):
        marks.append(int(input(f"Enter Subject {y+1} mark: ")))

    add_student(name, marks)


name = input("Enter student name to search: ")
student = search_student(name)

if student:
    print("Student Found")
    print("Name: ", student["name"])
    print("Marks: ", student["marks"])
    print("Average: ", student["average"])
else:
    print("Student not found")

print("Class Average:", class_average())

print("Top Performing Students:")
for x in top_students():
    print(x["name"], "(Avg:", x["average"], ")")
