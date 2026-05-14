import json
from datetime import datetime


def add_expense(expenses):
    title = input("Title:")
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = datetime.strptime(input("Date(YYYY-MM-DD): "),"%Y-%m-%d").date().isoformat()
    
    expense = {
		'title':title,
		'amount':amount,
		'category':category,
		'date':date
	}
    expenses.append(expense)
    save_data_helper(expenses)
    print("Expense Added!")
    

def view_all_expenses(expenses):
    for index, expense in enumerate(expenses):
        print("*"*60)
        print(f" {index+1}. {expense['title']}, {expense['amount']}, {expense['category']}, {expense['date']}")
        print("*"*60)
        
        
def filter_by_category(expenses):
    
    category = input("Enter category: ")
    for expense in expenses:
        if expense['category'] == category:
            print("-"*60)
            print(f"{expense['title']}, {expense['amount']}, {expense['category']}, {expense['date']}")
            print("-"*60)
        

def total_spending(expenses):
    total_spending = 0
    for expense in expenses:
        total_spending+=expense['amount']
        
    print("Total expenses: ",total_spending)
    return total_spending
        
    
def monthly_summary(expenses):
    
    month = input("Enter month: ")
    for expense in expenses:
        formatted_month = str(datetime.strptime(expense['date'],"%Y-%m-%d").month)
        if formatted_month==month:
            print("-"*60)
            print(f"{expense['title']}, {expense['amount']}, {expense['category']}, {expense['date']}")
            print("-"*60)
            

def load_expenses():
    try:
        with open('expenses.txt','r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
        

def save_data_helper(expenses):
    with open('expenses.txt','w') as file:
        json.dump(expenses,file)
        


def main():
    print("\nExpense Tracker | Choose an option")
   
    while True: 
        expenses = load_expenses()
        print("1. Add Expense")
        print("2. View all expenses")
        print("3. Filter by category")
        print("4. Calculate total spending")
        print("5. Monthly summary")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                add_expense(expenses)
                
            case '2':
                view_all_expenses(expenses)
            
            case '3':
                filter_by_category(expenses)
                
            case '4':
                total_spending(expenses)
                
            case '5':
                monthly_summary(expenses)
            
            case '6':
                break
        
            case _:
                print('Invalid choice')
                break
                
                
    
if __name__== "__main__":
    main()
  
