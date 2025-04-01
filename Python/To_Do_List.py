tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_num):
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: 1. Add 2. View 3. Remove 4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            remove_task(task_num)
        except ValueError:
            print("Invalid input.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
