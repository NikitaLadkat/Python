#Write a program which accept one number from user and return its factorial.

def fact():
    no =  int(input("Enter any number : "))
    r=1
    for i in range(1,no+1):
        r = r*i
    return r


print(fact())