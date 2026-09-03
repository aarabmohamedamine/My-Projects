from operations import add_contact,view_contact,search,valid_choice,delete_contact
from storage import load

def main():
    contact_list = load()
    while True :
        choice = valid_choice()
        if choice == 1 :
            add_contact(contact_list)
        elif choice == 2:
            view_contact(contact_list)
        elif choice == 3:
            if not contact_list:
               print("Contact list empty !!")
            else :
               print(search(contact_list))
        elif choice == 4:
            delete_contact(contact_list)
        elif choice == 5:
            break
        else : 
            print("Invalid choice .")


main()

