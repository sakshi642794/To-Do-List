# todo.py

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
