
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
                my_list.append(new_task)
                print("task added")


    elif user_choice == "v":
        if len(my_list)>0:
            list_title="My to-do list".center(50).title()
            print(f"\033[45m{list_title}\033[0m")
            for i, new_task in enumerate(my_list, start=1):
                print(i, new_task)
        else:
            print("\033[45mNothing found\033[0m")


