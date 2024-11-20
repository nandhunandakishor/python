# num=int(input("Enter the number"))
# if num>0:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime number")
#             break
#     else:
#         print(num,"prime number" )
# else:
#     print("The number is not greater than 1, hence not a prime number")

    

start=100
end=500
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)


