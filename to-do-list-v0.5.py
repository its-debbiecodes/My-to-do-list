
title= "Welcome to the To-Do List"
print(f"\n\033[44m{title}\033[0m")

to_do_list= []
while True:
    choice_1="Add tasks to To-Do List (press a)"
    choice_2="View to To-Do List (press v)"
    choice_3="Mark tasks as ✅ (press m)"
    choice_4="Delete task (press d)"
    print(f"\n{choice_1} \n{choice_2} \n{choice_3} \n{choice_4}")
    users_choice= input("What would you like to do? ")

    if users_choice == "a":
        print("Please enter your tasks (press e when done)")
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
            print("\n\033[43vmYou have no tasks added\033[0m")

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
                    task_index = int(mark_done) - 1
                    to_do_list[task_index]["✅"]= True

        else:
            print("\n\033[44mYou have no tasks in you To-do List\033[0m")

    elif users_choice == "d":
        if len(to_do_list) > 0:
            for i, task in enumerate(to_do_list, start=1):
                print(f"\033[32m{i}. {task['task']}\033[0m")

            print("What tasks number would you like to delete (enter f when done)")
            while True:
                delete_task = input("Enter tasks number: ")
                if delete_task == "f":
                    print("Great! Tasks deleted!")
                    break
                else:
                    task_index = int(delete_task) - 1
                    to_do_list.pop(task_index)
        else:
            print("\n\033[44mYou have no tasks in you To-do List\033[0m")



