import json as j

def load():
    try:

        with open("contact_manager/cm.json") as file:
            contact_list = j.load(file)
    except FileNotFoundError:
        contact_list = []

    return contact_list


def save(contact_list):
    with open("contact_manager/cm.json",'w') as file:
        j.dump(contact_list,file)

    return     



