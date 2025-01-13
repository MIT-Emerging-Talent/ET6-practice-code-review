def load_tasks(filename="todo.txt"):
    """Load tasks from a file."""
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="todo.txt"):
    """Save tasks to a file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    tasks.append(task)
    save_tasks(tasks)

def view_tasks(tasks):
    """Display all tasks."""
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nYour to-do list is empty.")

def delete_task(tasks):
    """Delete a task from the list."""
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
