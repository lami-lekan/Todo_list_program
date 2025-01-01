class ToDoList:
    def __init__(self):
        self.task = []
        self.completed_task = []

    # program main menu
    def main_menu(self):
        msg_display = "Hi! Welcome\nPress C to create a task\nPress V to view tasks\nPress M to mark completed task\nPress D " \
                      "to delete task\nPress E to exit program: "
        return input(msg_display).upper()

    # create a new task
    def create_task(self):
        while True:
            msg_display = "Type in a task[Enter B to go back]: "
            task = input(msg_display)
            if task.upper() == 'B':
                print("Going back to main menu")
                break
            self.task.append(task.title())
            print(f"Task '{task}' added to your list.")

    # display tasks
    def tasks_list(self):
        if not self.task:
            print('You have no task')
        else:
            print('Here are your tasks.')
            for index, item in enumerate(self.task, start=1):
                print(f"{index}. {item}")

    # remove completed task from task list
    def complete_task(self, num):
        try:
            if 1 <= num <= len(self.task):
                task_complete = self.task.pop(num - 1)
                self.completed_task.append(task_complete)
                print(f"Task '{task_complete}' marked as completed.")
            else:
                raise IndexError
        except ValueError:
            print("Please input numbers only.")
        except IndexError:
            print(f"Tasks number {num} doesn't exist. Please input correct task number.")

    # displays completed task
    def view_completed_task(self):
        if not self.completed_task:
            print("You got no task completed.")
        else:
            print("Completed task")
            for index, item in enumerate(self.completed_task, start=1):
                print(f"{index}. {item}")

    # delete task
    def delete_task(self, task_num):
        del self.task[task_num]

    # stops program completely
    def close_program(self):
        print("Existing program. Goodbye!")
        exit()