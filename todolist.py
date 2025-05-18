tasks = [] 
def add_task():
    task = input("Enter new task:\t")
    tasks.append(task)
    more = input("Do you want to add more tasks? (Y/N):\t")
    if more.upper() == 'Y':
        return add_task()
    elif more.upper() == 'N':
        return
    else: 
        print("Invalid answer :( \n...It was a YES or NO question!")
        return

def remove_task():
    try:
        task = int(input("Enter # of task you want to delete:\t"))
        if task in range(len(tasks)):
            confirm = input(f"Do you want to REMOVE '{tasks[task]}? (Y/N):\t'")
            if confirm.upper() == 'Y':
                del tasks[task]
                print(f"Task #{task} is removed :)")
            elif confirm.upper() == 'N':
                return
            else: 
                print("Invalid answer :( \n...It was a YES or NO question!")
                return remove_task()
        else: 
            print(f"Task #{task} is not in the to-do list... :(")
    except ValueError:
        print("Invalid number :(\n...Try again.")
        return remove_task()
    
def display_tasks():
    for i, item in enumerate(tasks):
        print(f"#{i} -> {item}")
print("Hello World :)")

while True:
    print("\n_______________________________________")
    print("1. Add new Task.")
    print("2. Remove existing Task.")
    print("3. Display all Tasks.")
    print("4. Exit program.")
    print("\n_______________________________________")
    action = input("\nWhat do you want to do?:\t")
    if action == '1':
        add_task()
    elif action == '2':
        remove_task()
    elif action == '3':
        display_tasks()
    elif action == '4':
        print("Thank you for using this program :)")
        break
    else:
        print("Invalid action. Try again..")
    