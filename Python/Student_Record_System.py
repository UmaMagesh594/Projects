import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
)
""")
conn.commit()

# Function to add a student
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print(f"Student {name} added successfully!")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    
    if records:
        print("\nStudent Records:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    else:
        print("No student records found.")

# Function to delete a student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print(f"Student with ID {student_id} deleted.")

# Menu for user input
while True:
    print("\nOptions: 1. Add Student  2. View Students  3. Delete Student  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        add_student(name, age, grade)
    
    elif choice == "2":
        view_students()
    
    elif choice == "3":
        view_students()
        student_id = input("Enter student ID to delete: ")
        delete_student(student_id)
    
    elif choice == "4":
        conn.close()
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again.")
