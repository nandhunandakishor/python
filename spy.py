a=int(input("Enter the number"))
sum=0
prod=1
n=a
while n>0:
    y=n%10
    sum=sum+y
    prod=prod*y
    n=n//10
if(sum==prod):
    print("Spy Number")
else:
    print("Not Spy Number")       
    
