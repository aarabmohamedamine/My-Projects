from storage import load_expenses 
from operations import add_expense ,view_expenses , total

def valid_choice():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice : "))
            return choice
        except ValueError :
            print('Try again !!')
def display_menu():
    print("------Expense Tracker------")
    print("1.Add an expense ")
    print("2.View all expenses ")
    print("3.Show total expenses ")
    print("4.Exit ")
def main():
    expenses = load_expenses()

    while True :
        choice = valid_choice()
        if choice == 1 :
            add_expense(expenses)
        elif choice == 2:
            if not expenses :
                print("no expenses found !! ")
            else:
                view_expenses(expenses)
        elif choice == 3:
            Total = total(expenses)
            print(f'The Total is : {Total}')
        elif choice == 4:
            break
        else :
            print("invalid choice")
main()