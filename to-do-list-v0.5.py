
title_text="My to do list".title().center(100)
print(f"\033[32m{title_text}\033[0m")
print("What would you like to do?")

my_list=[]


title= "Welcome to the To-Do List"
print(f"\n\033[44m{title}\033[0m")

to_do_list= []
while True:
    choice_1="Add tasks to To-Do List (press a)"
    choice_2="View to To-Do List (press v)"
    choice_3="Mark tasks as done (press m)"
    choice_4="Delete task (press d)"
    print(f"\n{choice_1} \n{choice_2} \n{choice_3} \n{choice_4}")
    users_choice= input("What would you like to do? ")

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

            for i, task in enumerate(to_do_list, start=1):
                print(f"\033[32m{i}. {task}\033[0m")

        else:
            print("\n\033[44mYou have no tasks added\033[0m")
