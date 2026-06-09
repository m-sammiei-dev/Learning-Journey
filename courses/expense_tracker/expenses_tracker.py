def add_expense(expense, amount, category):
    expense.append({'amount': amount,'category': category})

def remove_expense(expense, id):
    id -= 1
    expense.pop(id)
      
def print_expenses(expenses):
    for expence in expenses:
        print(f"amount: {expence['amount']}, category: {expence['category']}")

def total_expenses(expenses):
    # Extract 'amount' from each dictionary and return their sum
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):  
    # Filter expenses that match the specified category
    return list(filter(lambda expense: expense['category'] == category, expenses))

def calculate_category_percentage(expenses, category):
    total_all = total_expenses(expenses)
    if total_all == 0: return 0 
    
    category_expenses = filter(lambda expense: expense['category'] == category, expenses)
    total_cat = sum(map(lambda expense: expense['amount'], category_expenses))
    
    return int((total_cat / total_all) * 100)


expenses = []

def main():
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. Remove an expense')
        print('3. List all expenses')
        print('4. Show total expenses')
        print('5. Filter expenses by category')
        print('6. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
            
        elif choice == '2':
            id = int((input('Enter ID: ')))
            if id > 0 and id <= len(expenses):
                remove_expense(expenses, id)

        elif choice == '3':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '4':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '5':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
            expenses_from_category_percentage = calculate_category_percentage(expenses, category)
            print(f"Percentage of total expenses for this category: %{expenses_from_category_percentage}")
    
        elif choice == '6':
            print('Exiting the program.')
            break

main()
