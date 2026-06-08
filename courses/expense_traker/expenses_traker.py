def add_expence(expense, amount, category):
    expense.append({'amount': amount,'category': category})
    
def print_expenses(expenses):
    for expence in expenses:
        print(f"amount: {expence['amount']}, category: {expence['category']}")

def total_amount(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(map(lambda expense: expense['category'] == category, expenses))

expenses = []