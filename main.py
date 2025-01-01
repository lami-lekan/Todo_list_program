from todo_list import ToDoList

todo_list = ToDoList()
while True:
    choice = todo_list.main_menu()

    if choice == 'C':
        todo_list.create_task()
        todo_list.tasks_list()

    elif choice == 'V':
        while choice == 'V':
            todo_list.tasks_list()
            choice = input("Press B to go back to main menu: ").upper()

    elif choice == 'M':
        while choice == 'M':
            todo_list.tasks_list()    
            num = input("Input completed task number or 'B' to go back to main menu: ").upper()
            if num == 'B':
                break
            todo_list.complete_task(int(num))

    elif choice == 'D':
        todo_list.tasks_list()
        task_num = int(input('Enter the task number you want to remove: '))
        choice = input(f"Are you sure you want to delete {todo_list.task[task_num-1]}. Y/N: ").upper()
        if choice == 'N':
            print("Delete cancelled.")
            todo_list.main_menu()
        else:
            todo_list.delete_task(task_num-1)
            print('Task deleted succefully.')

    elif choice == 'E':
        todo_list.close_program()
    else:
        print("Invalid choice, try again!")
