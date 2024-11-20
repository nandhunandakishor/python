Expenses={}
print("\n Expense Tracker")
print("1.Add expense \n2.View expense \n3.Amount update \n4.exit")
while True:
    a=int(input("Enter your choice"))
    if a==1:
        category=input("Enter category")
        amount=int(input("Enter amount"))
        Expenses.update({"Category":category,"Amount":amount})
        print(Expenses)
    elif a==2:
        print(Expenses)
    elif a==3:
            category=input("Enter category to update")
            if category in Expenses.values():
                new_amount=int(input("Enter new amount"))
                Expenses.update({"Amount":new_amount})
                print(Expenses)
            else:
                print("Category not found")
    elif a==4:
        break
    else:
        print("Invaild choice")







    


    
