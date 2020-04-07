#Write a program which accept one number for user and check whether number is prime or not.

def prime():
    num =int(input("Enter any number : "))
    if num>0:
        for i in (2,num):
            if (num%i)==0:
                print("It is NOT a Prime")
                break
            else:
                print("It is a Prime")
                break
    else:
        print("Invalid")
prime()
