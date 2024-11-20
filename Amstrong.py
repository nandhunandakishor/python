
a=int(input("Enter the number"))
sum=0
n=a
x=len(str(a))
while n>0:
    y=n%10
    sum=sum+(y**x)
    n=n//10
if sum==a:
    print("Amstrong Number")
else:
    print("Not Amstrong")
    
    
