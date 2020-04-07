#6.Write a program which accept number from user and check whether that number is positive or negative or zero.

def check():
    no = int(input("Enter any number :"))
    if(no>0):
        print("Positive")
    elif (no<0):
        print("Negative")
    else:
        print("Zero")


check()