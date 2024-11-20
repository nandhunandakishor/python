# a=int(input('enter range'))
# for i in range(a):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()


# a=int(input("Enter range"))
# for i in range(a):
#     for j in range(a-i):
#         print("*",end="")
#     print()
        
#number printing
# a=int(input("Enter range"))
# for i in range(a):
#     for j in range(i+1):
#         print(j,end="")
#     print()


# a=int(input("Enter range"))
# for i in range(a):
#     for j in range(a-i):
#         print(j,end="")
#     print()


# a=int(input("Enter range"))
# for i in range(a):
#     for j in range(a):
#         print("*",end="")
#     print()


n = 5

for i in range(n):
    # Print leading spaces
    for j in range(n-i-1):
        print(' ', end=' ')
    
    # Print stars
    for j in range(2*i+1):
        print('*', end=' ')
    
    print()
