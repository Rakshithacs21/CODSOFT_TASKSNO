tasks =[]
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input ("enter your choice(1-5) :")
    if choice =="1":
        task=input("enter a new task:")
        tasks.append(task)
        print("task added successfully!")
    elif choice =="2":
        if len(tasks)==0:
            print(" no tasks found.")
        else:
            print("\nyour tasks:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                task_no = int(input("Enter task number to update: "))
                new_task = input("Enter the new task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                task_no = int(input("Enter task number to delete: "))
                tasks.pop(task_no - 1)
                print("Task deleted successfully!")
