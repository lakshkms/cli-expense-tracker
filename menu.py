from transaction import add_trans, history, balance, monthly

print(" "* 30)
print("=" * 30)
print("       EXPENSE TRACKER")
print("=" * 30)
print("1. add transaction")
print("2. view balance")
print("3. view transactions")
print("4. monthly summary")
print("5. exit")
print("=" * 30)

choice = int(input("enter choice: "))

if choice == 1:
    print("add transaction selected")
    add_trans()

elif choice == 2:
    print("view balance selected")
    print("-"*30)
    
    balance()
    
elif choice == 3:
    print("view transaction selected")
    history()

elif choice == 4:
    print("monthly summary selected")
    monthly()

elif choice == 5:
    print("goodbye!")
    exit()

else:
    print("invalid choice")