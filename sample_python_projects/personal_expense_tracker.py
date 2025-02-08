import csv
import os
import time

total_expense_list = []
current_date = ""
file_output_path = 'expenses.csv'

def validate_date(date):
    current_year, current_month, current_day = current_date.split('-')
    # this function will be used to validate the date
    if len(date) != 10:
        return False
    else:
        year, month, day = date.split('-')
        if len(month) == 1:
            month = '0' + month
        elif len(day) == 1:
            day = '0' + day
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            print("Invalid date format")
            return False
        if int(month) < 1 or int(month) > 12:
            print("Invalid month")
            return False
        if int(day) < 1 or int(day) > 31:
            print("Invalid day")
            return False
        if int(year) < 1900 or int(year) > int(current_year):
            print("Invalid year")
            return False
        if int(year) == int(current_year) and int(month) > int(current_month):
            print("Invalid month")
            return False
        if int(year) == int(current_year) and int(month) == int(current_month) and int(day) > current_day:
            print("Invalid day")
            return False
    return True

def validate_expense(date_of_expense, category, amount_spend, description):
    # this function will be used to validate the input data
    if not validate_date:
        return False
    if len(category) == 0 or amount_spend <= 0 or len(description) == 0:
        return False
    return True

def add_expense():
    # this function will be used to add an expense to the list
    # first check if the file exists if yes load the data else create a new file
    date_of_expense = input("Enter the date of the expense (YYY-MM-DD) format: ")
    category = input("Enter the category of the expense: ")
    amount_spend = float(input("Enter the amount spent: "))
    description = input("Enter the description of the expense: ")
    if validate_expense(date_of_expense, category, amount_spend, description):
        total_expense_list.append({'date': date_of_expense, 'category': category, 'amount': amount_spend, 'description': description})
        print("Expense added successfully")
    else:
        print("Invalid expense. Please try again")

def view_expenses():   
    # this function will be used to view the expenses
    print("The complete expenses:")
    for expense in total_expense_list:
        if validate_expense(expense['date'], expense['category'], expense['amount'], expense['description']):
            print(expense)
        else:
            print(f"Invalid expense: {expense}")
    response = input("Do you want to view the total expenses for only this month? (Y/N): ")
    if response.upper() == 'Y' or response.upper() == 'YES':
        for expense in total_expense_list:
            year, month, _= expense['date'].split('-')
            if int(year) == int(current_date.split('-')[0]) and int(month) == int(current_date.split('-')[1]):
                print(expense)

def get_monthly_budget():
    # this function will be used to get the monthly budget
    monthly_budget = float(input("Enter the monthly budget: "))
    return monthly_budget

def get_total_expense():
    total_expense = 0
    for expense in total_expense_list:
        year, month, _= expense['date'].split('-')
        if int(year) == int(current_date.split('-')[0]) and int(month) == int(current_date.split('-')[1]):
            total_expense += expense['amount']
    return total_expense
    
def track_budget():
    # this function will be used to track the budget
    monthly_budget = get_monthly_budget()
    total_expense = get_total_expense()
    print(f"Total expenses for this month: {total_expense}")
    if total_expense > monthly_budget:
        print(f"You have exceeded your budget by: {total_expense - monthly_budget}")
    else:
        print(f"You have {monthly_budget - total_expense} left for the month")

def save_expenses():
    # this function will be used to save the expenses to a file
    with open(file_output_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for expense in total_expense_list:
            writer.writerow(expense)

def init():
    # this function will be used to initialise the total_expense_list
    # first check if the file exists if yes load the data
    date_time = time.localtime()
    global current_date
    current_date = f"{date_time.tm_year}-{date_time.tm_mon}-{date_time.tm_mday}"
    if os.path.isfile(file_output_path):
        with open(file_output_path, 'r') as file:
            reader = csv.DictReader(file) 
            for row in reader:
                total_expense_list.append({'date': row['date'], 'category': row['category'], 'amount': float(row['amount']), 'description': row['description']})
    return current_date

def main():
    # this can be used to display an interactive menu\
    current_date = init()
    print("Welcome to the Personal Expense Tracker")
    print(f"Today's date is: {current_date}")

    while(True):
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save expenses to a file")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == '__main__':
    main()