contacts={}
print(("1.Insert \n2.Update \n3.View \n4.Delete \n5.Exit"))
while True:
    a=int(input("Select an option"))
    if a==1:
        Name=input("Enter name")
        Phone=int(input("Enter phone number"))
        contacts.update({"name":Name,"phone":Phone})
        print(contacts)
       
    elif a==2:
        name=input("Enter name")
        if name in contacts.values():
                New_phone=int(input("Enter phone number"))
                contacts.update({'phone':New_phone})
                print(contacts)
        else:
             print('No contact')

    elif a==3:
        print(contacts)
    elif a==4:
         name=input('Enter name to delete')
         if name in contacts:
              del contacts[name]
              print(contacts)
         else:
              print("Name not found")
    elif a==5:
         break
    else:
     print("Invaild choice")