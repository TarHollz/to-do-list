tasks = []

def add_task():
    while True:
        task = input("Enter new task:\t").strip()
        if task:
            tasks.append(task)
            print(f"Task '{task}' added.")
        else:
            print("Empty task ignored.")
        
        more = input("Do you want to add more tasks? (Y/N):\t").strip().lower()
        if more == 'n':
            break
        elif more != 'y':
            print("invalid input. Ending task addition.")
            break

def remove_task():
    display_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the # of the task you want to delete:\t"))
        if 0 <= task_num < len(tasks):
            confirm = input(f"Do you want to REMOVE '{tasks[task_num]}'? (Y/N):\t").strip().lower()
            if confirm == 'y':
                removed = tasks.pop(task_num)
                print(f"Task '{removed}' removed.")
            elif confirm == 'n':
                print("Task not removed.")
            else:
                print("Invalid confirmation input.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"#{i}: {task}")

def main():
    print("Welcome to the To-Do List App!")

    while True:
        print("\n_______________________________________")
        print("1. Add new Task.")
        print("2. Remove existing Task.")
        print("3. Display all Tasks.")
        print("4. Exit program.")
        print("_______________________________________")

        choice = input("What do you want to do?:\t").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
