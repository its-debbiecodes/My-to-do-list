
title_text="My to do list".title().center(100)
print(f"\033[32m{title_text}\033[0m")
print("What would you like to do?")

my_list=[]


while True:
    option_1= "Add to my to-do list (press a)"
    option_2= "view my to-do list (press v)"
    option_3 = "Mark task as done (press m)"
    option_4 = "Delete task (press d)"
    print(f"\n{option_1}\n{option_2}\n{option_3}\n{option_4}")
    user_choice = input("\nWhat would you like to do? ")

    if user_choice == "a":
        print("If done adding task, press f")
        while True:
            new_task=input("Enter task: ")
            if new_task == "f":
                print("Added all tasks")
                break
            else:
                my_list.append({"task":new_task, "done":False})
                print("task added")


    elif user_choice == "v":
        if len(my_list)>0:
            list_title="My to-do list".center(50).title()
            print(f"\033[45m{list_title}\033[0m")
            for i, new_task in enumerate(my_list, start=1):
                print(i, new_task)
        else:
            print("\033[45mNothing found\033[0m")

choice_1="Add tasks to To-Do List (press a)"
choice_2="View to To-Do List (press v)"
choice_3="Mark tasks as done (press m)"
choice_4="Delete task (press d)"
print(f"\n{choice_1} \n{choice_2} \n{choice_3} \n{choice_4}")
users_choice= input("What would you like to do?")

    if users_choice == "a":
        print("Please enter your tasks (press e when done)")
        while True:
            task = input("Enter Tasks: ")
            if task == "e":
                print("\n\033[35mTask added!\033[0m")
                break
            else:
                to_do_list.append(task)

    elif users_choice == "v":
        if len(to_do_list) > 0:
            list_title= "To-Do List"
            print(f"\n\033[42m{list_title}\033[0m")


