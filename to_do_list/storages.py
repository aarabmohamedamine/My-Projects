import json


def save_tasks(tasks):
    with open("to_do_list/tasks.json",'w') as file:
        json.dump(tasks,file)
    return
def load_tasks():
    try :
            with open('to_do_list/tasks.json') as file :
              tasks = json.load(file)
    except FileNotFoundError :
        tasks = []
    return tasks


