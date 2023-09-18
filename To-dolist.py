task = []
def addtask(task1):
    task.append(task1)
    print(f"Task succesfully '{task1}' added!")

def listtasks():
    if task:
        print("List:")
        for i, j in enumerate(task, 1):
            print(f"{i}. {j}")
    else:
        print("Your List is empty.")

def marktaskandremove(task_index):
    if (1 <= task_index <= len(task)):
        task1 = task[task_index - 1]
        print(f"Task '{task1}' marked as done!")
        del task[task_index - 1]
    else:
        print("Invalid task index.")

while(1):
    print("Options:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as done")
    print("4. Quit")
    ch=input("Enter your choice 1,2,3,4: ")

    if ch == "1":
        task1 = input("Enter the task: ")
        addtask(task1)
    elif ch == "2":
        listtasks()
    elif ch == "3":
        task_index = int(input("Enter the task number to mark as done: "))
        marktaskandremove(task_index)
    elif ch == "4":
        print("bye")
        break
    else:
        print("Invalid choice")