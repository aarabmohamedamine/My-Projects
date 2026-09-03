from storages import save_tasks


def add_task(tasks):
    
    task_name = input('Enter the task : ')
    task_dictionary = {"Title" : task_name, "status" : "Pending" 

    }
    tasks.append(task_dictionary)
    save_tasks(tasks)
    print("Task added successfully")
     
def view_tasks(tasks):
    for index,task in enumerate(tasks,start=1):
        print(f"{index} . {task['Title']} - [{task['status']}]")
    return
def delete_task(tasks):
    view_tasks(tasks)
    index = get_index(tasks)
    del tasks[index]
    save_tasks(tasks)
def mark_done(tasks):
    
    view_tasks(tasks)
    index = get_index(tasks)
    task_dictionary = tasks[index]
    task_dictionary['status'] = 'Done'
    save_tasks(tasks)

def get_index(tasks):
    while True :
        try :            
            task_number = int(input("enter the task number : "))
            if task_number > 0 and task_number <= len(tasks):
                return task_number-1
                
            else :  
                print('number invalid')
        except ValueError:
            print("error.")
