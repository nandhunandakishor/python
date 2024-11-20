Account_Balance=1000
print("ATM Machine")
print("1.Deposit")
print("2.Withdraw")
print("3.Account Balance")

choice=int(input("Enter your choice: "))
if choice==1:
    deposit=int(input("Enter deposit amount"))
    Account_Balance=Account_Balance+deposit
    print("Current balance is:",Account_Balance)
elif choice==2:
    withdraw=int(input("Enter amount"))
    if Account_Balance<=withdraw:
        Account_Balance=Account_Balance-withdraw
        print("Current balance:",Account_Balance)
    else:
        print("Insufficient Balance")          
elif choice==3:
    print("Your account balance",Account_Balance)
    

