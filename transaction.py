import json
import calendar

def load():
    with open("data.json", "r") as file:
        data = json.load(file)
        return data
    
def add_trans():
    data = load()

    date = int(input("enter date: "))
    month = int(input("enter month (in numbers): "))
    month = calendar.month_name[month]
    year = int(input("enter year: "))

    print("-" * 16)

    if data["balance"] is None:
        monthly_income = float(input("enter monthly income: "))
        balance = monthly_income

    else:
        balance = data["balance"]
        print("balance:", balance)

    print("-" * 16)

    print("a = credit")
    print("b = debit")

    op = input("enter operation: ")

    print("-" * 16)

    amount = float(input("enter amount: "))

    print("-" * 16)

    category = input("enter category: ")

    transaction = {
        "month": month,
        "date": date,
        "operation": op,
        "amount": amount,
        "category": category,
        "year": year,
    }

    data["transactions"].append(transaction)

    if transaction["operation"] == "a":
        operation_type = 'CREDIT'
        print(f"credit: {amount}")
        result = balance + amount
        print(f"new balance: {result}")

    elif transaction["operation"] == "b":
        operation_type = 'DEBIT'
        print(f"debit: {amount}")
        result = balance - amount
        print(f"new balance: {result}")

    else:
        print("invalid")
        print(balance)
        return

    data["balance"] = result

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print(transaction)

def balance():
    
    data = load()
    print("your balance: ",data["balance"])

def history():

    data = load()

    print(f"{'DATE':<20}{'OPERATION':<10}{'AMOUNT':<15}{'CATEGORY':>20}")
    print("-"*60)

    for transaction in data["transactions"]:

     date = f"{transaction['date']} {transaction['month']} {transaction['year']}"

     if transaction["operation"] == "a":
            operation_type = "CREDIT"

     elif transaction["operation"] == "b":
            operation_type = "DEBIT"

     print(f"{date:<20}{operation_type:<10}{transaction['amount']:<15.2f}{transaction['category']:>20}")

def monthly():

    data = load()
    
    month = int(input("enter month: "))
    month = calendar.month_name[month]
    year = int(input("enter year: "))
           
    credits = []
    debits = [] 

    for transaction in data["transactions"]:
                
            if transaction["month"] == month and transaction["year"] == year:

                if transaction["operation"] == "a":
                    credits.append(transaction["amount"])
                
                elif transaction["operation"] == "b":
                    debits.append(transaction["amount"])

    total = sum(credits)
    total_d = sum(debits)

    print("="*30)
    title = f"{month.upper()} {year}"
    print(f"{title:^30}")
    print("="*30)

    print("total credit: ", total)
    print("total debit: ", total_d)

    print("-"*30)
    net = total - total_d
    print("net change: ", net)
    print("="*30)