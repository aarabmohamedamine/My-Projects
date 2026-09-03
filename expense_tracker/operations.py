from storage import save_expense


def add_expense(expenses):
    while True :
        try :
            amount = int(input("Enter the amount : "))
            category = input("Enter the category : ")
            description = input("Enter the description : ")
            expense = {'amount':amount , 'category' : category , 'description' : description }
            expenses.append(expense)
            print("expense added !")
            save_expense(expenses)
            break

        except ValueError:
            print("try agan !! ")
def view_expenses(expenses):
    for expense in expenses:
        print(expense)
def total(expenses):
    Total  =  0
    for expense in expenses:
        Total = Total + expense['amount']

    return Total
