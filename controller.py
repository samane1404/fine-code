from model import ToDoModel
from view import ToDoView

class ToDoController:
    def __init__(self):
        self.model = ToDoModel()
        self.view = ToDoView()

    def run(self):
        self.view.show_welcome()
        username = self.view.prompt_for_username()
        user_id = self.model.get_user_id(username)
        if not user_id:
            self.model.add_user(username)
            user_id = self.model.get_user_id(username)

        while True:
            self.view.show_tasks(self.model.get_tasks(user_id))
            print("\nOptions:")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                task = self.view.prompt_for_task()
                self.model.add_task(user_id, task)
            elif choice == "2":
                task_id = int(self.view.prompt_for_task_update())
                new_status = self.view.prompt_for_new_status()
                self.model.update_task(task_id, new_status)
            elif choice == "3":
                task_id = int(self.view.prompt_for_task_deletion())
                self.model.delete_task(task_id)
            elif choice == "4":
                self.view.show_goodbye()
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    controller = ToDoController()
    controller.run()
