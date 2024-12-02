class ToDoView:
    def show_welcome(self):
        print("Welcome to the To-Do List Manager")

    def prompt_for_username(self):
        return input("Enter your username: ")

    def show_tasks(self, tasks):
        if tasks:
            print("Your Tasks:")
            for task in tasks:
                print(f"{task[0]}. {task[1]} - {task[2]}")
        else:
            print("You have no tasks.")

    def prompt_for_task(self):
        return input("Enter a task: ")

    def prompt_for_task_update(self):
        return input("Enter the task number to update: ")

    def prompt_for_new_status(self):
        return input("Enter the new status (Pending/Completed): ")

    def prompt_for_task_deletion(self):
        return input("Enter the task number to delete: ")

    def show_goodbye(self):
        print("Goodbye!")
