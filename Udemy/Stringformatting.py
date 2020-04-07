
#Accept the Name(String from user and display in the format.



def accept():
    c= str(input("Enter your name : "))
   # p = "%s Hello !"%c
    p = f"{c} Hello!"
    print(p)


accept()


#Accept multiple values fro user and execute it :
def Fullname():
    name = str(input("Enter your name : "))
    surname = str(input("Enter your Surname : "))
    when = " How are you...!"
    p = f"%s %s Hello {when}!"%(name,surname)
   # p = f"{c} Hello!"
    print(p)


#accept()
Fullname()



