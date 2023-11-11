class Task_Manager:
    #---------------------------------
    def __init__(self):
        self.tasks = []
    #--------------------------------------
    def add_task(self, title, description):
        task = {"title": title, "description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task {title} added successfully!")
    #------------------------------------------
    def mark_completed(self):
        if self.tasks:
            task = self.tasks.pop()
            task["completed"] = True
            print(f"Task {task['title']} marked as completed.")
        else:
            print("No tasks available for completion.")

    #--------------------------------
    def diplay_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("-------------------Your Current Task----------------------")
            for i, Add_Task in enumerate(self.tasks):
                if Add_Task["completed"]:
                    status = "completed"
                else:
                    status = "not completed"
                print("========================================================")
                print(f"{i + 1}.Title: {Add_Task['title']} \n  Description: {Add_Task['description']} \n  Status: {status}")
                print("========================================================")

TaskManager = Task_Manager()
#------------------------------------------------------

while True:
    print("\n Task Manager Menu: ")
    print("--------------------------")
    print("1. Add Task ")
    print("2. Mark as Completed")
    print("3. List of Task")
    print("4. Exit")

    choices = input("Choose what you want to do: ")

    if choices == "1":
        title = input("Enter Task Title:")
        description = input("Enter Description for the Task:")
        TaskManager.add_task(title,description)
    elif choices == "2":
        TaskManager.diplay_task()
        Task = int(input("Enter the Task you want to mark as completed:"))
        TaskManager.mark_completed()
    elif choices == "3":
        TaskManager.diplay_task()
    elif choices == "4":
        print("Exiting the Task Manager....")
        break
    else:
        print("Invalid choice. Please select a valid option.")