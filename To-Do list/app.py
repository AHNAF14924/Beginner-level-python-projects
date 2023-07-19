import os

def add_task(task):
    tasks.append(task)
    save_tasks()

def edit_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        save_tasks()
    else:
        print("Invalid index!")

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks()
    else:
        print("Invalid index!")

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    else:
        return []

def main():
    global tasks
    tasks = load_tasks()

    while True:
        print("\n1. Add task")
        print("2. Edit task")
        print("3. Delete task")
        print("4. Display tasks")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            index = int(input("Enter the index of the task to edit: ")) - 1
            new_task = input("Enter the new task: ")
            edit_task(index, new_task)
            print("Task edited successfully.")
        elif choice == "3":
            index = int(input("Enter the index of the task to delete: ")) - 1
            delete_task(index)
            print("Task deleted successfully.")
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Quitting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()