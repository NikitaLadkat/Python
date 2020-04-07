#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def TF ():
    no = int(input("Enter any number : "))
    c = no%5==0
    while True:
        print(c)
        break

TF()