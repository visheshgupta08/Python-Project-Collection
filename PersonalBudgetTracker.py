import os
import json

transaction = []

def load_data():
    global transaction
    if os.path.isfile("budget.txt"):
        with open("budget.txt", 'r') as l:
            transaction = json.load(l)

def add_income():
    global transaction
    amount1 = float(input("Income amount: "))
    dict1 = {"type": "Income", "amount": amount1}
    transaction.append(dict1)

def add_expenses():
    global transaction
    amount2 = float(input("Expenses amount: "))
    category = input("category: ")
    dict2 = {"type": "Expenses", "amount": amount2, "category": category}
    transaction.append(dict2)

def view_balance():
    global transaction
    total_income = 0
    total_expenses = 0
    for i in transaction:
        if i["type"] == "Income":
            total_income += i["amount"]
        elif i["type"] == "Expenses":
            total_expenses += i["amount"]
    print("total_income: ", total_income)
    print("total_expenses: ", total_expenses)
    print("Available Balance: ", total_income - total_expenses)

def save_data():
    global transaction
    with open("budget.txt", 'w') as f:
        json.dump(transaction, f)
    print("\n💾 Data successfully save ho gaya hai! Program band ho raha hai. Bye! 👋\n")

load_data()
while True:
    work = input(" Press 1 for Add income or Press 2 for Add Expenses or Press 3 for view Available balance or Press 4 for Quit and save data: ")
    if work == "1":
        add_income()
    elif work == "2":
        add_expenses()
    elif work == "3":
        view_balance()
    elif work == "4":
        save_data()
        break
