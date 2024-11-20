#match
# import re
# pattern="Good"
# if re.match(pattern,"Good evening,How are you"):
#     print("Yes")
# else:
#     print("Sorry") 


#search
# import re
# pattern="good"
# if re.search(pattern,"hi good evening , how are you"):
#     print("yes")
# else:
#     print("sorry")


#findall
import re
pattern="jithin"
b=re.findall(pattern,"jdjmkdjkjithin joi jithin maki jithinjin")
print(b)
c=len(b)
d={}
d.update({pattern:c})
print(c)
print(d)

#to substitute / edit or change
# import re
# str="hey prabhu jithin who are you"
# pattern="prabhu"
# b=re.sub(pattern,"hari ram",str)
# print(b)

# import re
# a="hi adarsh who are you"
# pattern="who"
# c=re.sub(pattern,"how",a)
# print(c)


