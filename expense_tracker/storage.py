import json
def load_expenses():
    try:
        with open('expense_tracker/expenses.json') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    return expenses

def save_expense(expenses):
    with open('expense_tracker/expenses.json', 'w')as file:
        json.dump(expenses,file)