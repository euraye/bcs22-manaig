class Task_Manager:
    def __init__(self):
        self.tasks_stack = []

    def add_task(self, title, description):
        task = [title, description, False]
        self.tasks_stack.append(task)
        print(f"Task {title} added successfully!")

    def mark_completed(self):
        if self.tasks_stack:
            task = self.tasks_stack.pop()
            task[2] = True
            self.tasks_stack.append(task)  # Re-add the task with completed flag
            print(f"Task {task[0]} marked as completed.")
        else:
            print("No tasks available for completion.")

    def display_task(self):
        if not self.tasks_stack:
            print("No tasks available.")
        else:
            print("-------------------Your Current Task----------------------")
            for i, task in enumerate(reversed(self.tasks_stack)):
                status = "completed" if task[2] else "not completed"
                print("========================================================")
                print(f"{i + 1}. Title: {task[0]} \n  Description: {task[1]} \n  Status: {status}")
                print("========================================================")


TaskManager = Task_Manager()

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
        TaskManager.add_task(title, description)
    elif choices == "2":
        TaskManager.display_task()
        Task = int(input("Enter the Task you want to mark as completed:"))
        TaskManager.mark_completed()
    elif choices == "3":
        TaskManager.display_task()
    elif choices == "4":
        print("Exiting the Task Manager....")
        break
    else:
        print("Invalid choice. Please select a valid option.")
