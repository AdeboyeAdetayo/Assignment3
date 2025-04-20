students = {}

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    score = input("Enter score: ")
    students[name] = {"age": age, "score": score}
    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
    for name, info in students.items():
        print(f"Name: {name}, Age: {info['age']}, Score: {info['score']}")

def search_student():
    name = input("Enter name to search: ")
    if name in students:
        print(f"Found: Name: {name}, Age: {students[name]['age']}, Score: {students[name]['score']}")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student\n2. View All\n3. Search\n4. Delete\n5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
