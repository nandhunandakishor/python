# a=input("Enter the string")
# n=(a[::-1])
# if n==a:
#     print("Palindrome")
# else:
#     print("not")


a=int(input("Enter the number"))
b=0
n=a
while(a>0):
    s=a%10
    b=b*10+s
    a=a//10
if n==b:
    print("Palindrome")
else:
    print("not")
    

# def palindrome(a):
#     b=0
#     n=a
#     s=0
# while(a>0):
#     s=a%10
#     b=b*10+s
#     a=a//10
# if n==b:
#     print("Palindrome")
# else:
#     print("not")



# palindrome(121)

    

