# a=input("Enter a word")
# b=len(a)
# s=0
# for i in range(b):
#     if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="O" or a[i]=="U":
#         s=s+1
# print(a,"Has ",s,"vowels")


# a=input("Enter word")
# b=[]
# c=["A","a","E","e","I","i","O","o","U","u"]
# for i in a:
#     if i in c:
#         b.append(i)
# print(b)
# for i in sorted(set(b)):
#     print("{} occurs {} Times".format(i,b.count(i)))


# word=input("Enter word")
# result=""
# vowels=["A","a","E","e","I","i","O","o","U","u"]
# for i in word:
#     if i not in vowels:
#         result=result+i
# print(result)

# word=input("Enter word")
# result=""
# special='''@#$%^&*()?'''
# for i in word:
#     if i not in special:
#         result=result+i
# print(result)


# a=input("Enter string")
# alphabates=""
# numbers=""
# special=""

# for i in a:
#     if i.isalpha():
#         alphabates=alphabates+i
#     elif i.isdigit():
#         numbers=numbers+i
#     else:
#         special=special+i

# print("Alphabates",alphabates)
# print("Numbers",numbers)
# print("Special",special)



def add_without_plus(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Example usage:
num1 = 10
num2 = 5
result = add_without_plus(num1, num2)
print(result)  # Output: 15