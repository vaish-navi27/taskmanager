import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task():
    task = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    tasks.append({"task": task, "deadline": deadline, "completed": False})
    save_tasks(tasks)
    print("Task added!")

def list_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']} (Due: {task['deadline']})")

def mark_completed():
    list_tasks()
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")

tasks = load_tasks()

while True:
    print("\n1. Add Task  2. List Tasks  3. Mark Completed  4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        break
    else:
        print("Invalid option. Try again.")
