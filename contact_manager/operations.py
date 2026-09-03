from storage import save
import datetime as d
def display_menu():

    print('1.Add contact ')
    print('2.View all contacts')
    print('3.Search for a contact')
    print('4.Delete a contact')
    print('5.Exit')
def valid_choice():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice : "))
            return choice
        except ValueError :
            print('Try again !!')
def get_index(contact_list):
    while True :
        try :            
            contact_index = int(input("enter the contact index : "))
            if contact_index > 0 and contact_index <= len(contact_list):
                return contact_index-1
                
            else :  
                print('number invalid')
        except ValueError:
            print("error.")

def add_contact(contact_list):
    name = input("Enter the name : ")
    number = int(input("enter the phone number : "))
    email = input("Enter the email : ")
    date = d.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = {'name' : name ,'number' : number , 'email' : email , 'date' : date}
    contact_list.append(data)
    save(contact_list)
    print("Contact added successfully !! ")
def view_contact(contact_list):
    if not contact_list:
        print('No contact founded .')
    else :
        for item in contact_list :
            print(item)
def search(contact_list):
    
        name = input('Enter the Name : ')
        for element in contact_list:
            if name.lower() == element['name'].lower():
                return [element['number'],element['email']]

        return 'No results'
def delete_contact(contact_list):
    if not contact_list:
        print("Contact list empty !!")
    else :
        view_contact(contact_list)
        contact_index = get_index(contact_list)
        del contact_list[contact_index]
        print("Contact deleted .")
        save(contact_list)


