
title= "Welcome to the To-Do List"
print(f"\n\033[44m{title}\033[0m")

to_do_list= []
while True:
    choice_1="Add tasks to To-Do List (press a)"
    choice_2="View to To-Do List (press v)"
    choice_3="Mark tasks as ✅ (press m)"
    choice_4="Delete task (press d)"
    choice_5="Exit (press e)"
    print(f"\n{choice_1} \n{choice_2} \n{choice_3} \n{choice_4} \n{choice_5}")
    users_choice= input("\nWhat would you like to do? ")

    if users_choice == "a":
        print("\nPlease enter your tasks (press f when done)")
        while True:
            task = input("Enter Tasks: ")
            if task == "f":
                print("\n\033[35mTask added!\033[0m")
                break
            else:
                to_do_list.append({"task" : task, "✅" : False})

    elif users_choice == "v":

        if len(to_do_list) > 0:
            list_title= "To-Do List"
            print(f"\n\033[43m{list_title}\033[0m")

            for i, task in enumerate(to_do_list, start=1):

                if task["✅"]:
                    print(f"\033[32m{i}. {task['task']}✅\033[0m")
                else:
                    print(f"\033[32m{i}. {task['task']}\033[0m")

        else:
            print("\n\033[42mYou have no tasks added\033[0m")

    elif users_choice == "m":
        if len(to_do_list) > 0:
            for i, task in enumerate(to_do_list, start=1):
                print(f"\033[32m{i}. {task['task']}\033[0m")

            print("What tasks number would you like to mark as ✅ (enter f when done)")
            while True:
                mark_done = input("Enter tasks number: ")
                if mark_done == "f":
                    print("Tasks done ✅. Good job!")
                    break
                else:
                    try:
                        mark_index = int(mark_done) - 1
                        if mark_index< 0 or mark_index > len(to_do_list):
                            print("\033[31mTask number doesn't exist\033[0m")
                        else:
                            task_index = int(mark_done) - 1
                            to_do_list[task_index]["✅"]= True
                    except ValueError:
                        print("\033[31mPlease enter a valid task number!\033[0m")
        else:
            print("\n\033[42mYou have no tasks in you To-do List\033[0m")

    elif users_choice == "d":
        if len(to_do_list) > 0:

            print("What tasks number would you like to delete (enter f when done)")
            while True:
                for i, task in enumerate(to_do_list, start=1):
                    print(f"\033[32m{i}. {task['task']}\033[0m")
                delete_task = input("Enter tasks number: ")
                if delete_task == "f":
                    print("Great! Tasks deleted!")
                    break
                else:
                    try:
                        task_index = int(delete_task) - 1
                        if task_index < 0 or task_index >= len(to_do_list):
                            print("\033[31mTask number doesn't exist\033[0m")

                        else:
                            to_do_list.pop(task_index)
                            print("task deleted!")

                    except ValueError:
                        print("\033[31mPlease enter a valid task number!\033[0m")
        else:
            print("\n\033[42mYou have no tasks in you To-do List\033[0m")

    elif users_choice == "e":
        print("\n\033[32mThanks for using The To-Do List\033[0m")
        break

    else:
        print(f"\033[42mOops! looks like you have a different option in mind, Please try again.\033[0m")
        continue



