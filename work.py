#Two number divide with out using * 
# x=10
# y=3
# print(x//y)

# a=["orange","apple"]
# b=["grapes","kiwi"]

# c=[a,b]
# print(c[0][1])

# a=[1,7,5,[9,4,3],6,8]
# b=a.index([0])
# print(b)

#list and word count
# a=["orange","apple","grapes","mango"]
# for i in a:
#     b=len(i)
#     print(i,b)

#Addition using while loop
# num1=10
# num2=20
# sum=0
# counter=0
# while counter<1:
#     sum=num1+num2
#     counter+=1
# print(f"The sum of {num1} and {num2} is {sum}")
   

# string = input("Please Enter a string: ")
# x = {}
# for i in string:
#     if i in x:
#         x[i] += 1
#     else:
#         x[i] = 1
# z = max(x.values())
# for i in x:
#     if x[i] == z:
#         print(i, end=' ')



# word="aaple"
# common=max(word,key=word.count)
# print(common)


# word="aaple"
# c=word.count
# b=max(c)
# print(c)


a=int(input('enter range'))
for i in range(a):
    if i == a-1:
        print('* ' *a )
    else:
        print('*')