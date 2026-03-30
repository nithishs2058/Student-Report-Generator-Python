import csv

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

def add_student():
    name = input("Enter Student Name: ")
    marks = []

    for i in range(3):
        m = int(input(f"Enter mark {i+1}: "))
        marks.append(m)

    total = sum(marks)
    avg = total / 3
    grade = calculate_grade(avg)

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, total, avg, grade])

    print("Student record added successfully!")

def display_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Student Report ---")
            for row in reader:
                print(f"Name: {row[0]}, Total: {row[1]}, Avg: {row[2]}, Grade: {row[3]}")
    except FileNotFoundError:
        print("No records found!")

while True:
    print("\n1. Add Student\n2. Display Records\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    else:
        break