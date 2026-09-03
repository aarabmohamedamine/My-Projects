from operation import add_task,view_tasks,mark_done,delete_task,get_index
from storages import load_tasks

import os



def display_menu():
    print("------Menu------")
    print("1.add task ")
    print("2.View task")
    print("3. Mark Task as Done")
    print("4.delete task")
    print("5.clear all")
    print("6.exit")
    return 



def main():

    tasks = load_tasks()
    while True :
        display_menu()
        try :
            choice = int(input("enter your choice : ")) 
        except ValueError :
            print("try again !! ")
            continue
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            if not tasks :
                print("tasks list empty!!")
            else :
                view_tasks(tasks)
        elif choice == 3:
            if not tasks :
                print("tasks list empty!!")
            else :
                mark_done(tasks)  
        elif choice == 4:
            if not tasks :
                print("tasks list empty!!")
            else :
                delete_task(tasks)
        elif choice == 5:
            if not tasks :
                print("tasks list empty!!")
            else :
                os.remove('tasks.json')
        elif choice == 6 :
            break
        else :
            print("invalid choice")
 
main()