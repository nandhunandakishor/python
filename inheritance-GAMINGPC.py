class student:
    def __init__(self,name,hodname,college):
        self.name=name
        self.hodname=hodname
        self.college=college
    def getdata(self):
        self.name=input("enter the student name")

class hod(student):
    def data1(self):
        self.hodname=input("Enter the hodname")
    def putdata(self):
        self.college=input("Enter Collage")
    def display(self):
        print("Student name is",self.name)
        print("your hod name is",self.hodname)
        print("Collage name is ",self.college)
        
obj=hod("","","")
obj.getdata()
obj.data1
obj.putdata()
obj.display()


# class student:
#     def __init__(self,name,hodname,collage):
#         self.name=name
#         self.hodname=hodname
#         self.collage=collage
#     def getdata(self):
#         self.name=input("Enter your name")

# class hod(student):
#     def data1(self):
#         self.hodname=input("Enter your hodname")
#     def putdata(self):
#         self.collage=input("Enter your collage")
#     def display(self):
#         print("student name is ",self.name)
#         print("hod name is ",self.hodname)
#         print("collage is ",self.collage)

# obj=hod("","","")
# obj.getdata()
# obj.data1()
# obj.putdata()
# obj.display()

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lastname = lname

#     def getdata(self):
#         self.fname=input("Enter your first name")
#         self.lastname=input("Enter your last name")
  
#     def display(self):
#         print(self.fname, self.lastname)


# x = Person("", "")
# x.getdata()
# x.display()








        