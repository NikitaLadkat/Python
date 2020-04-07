#Write a program which contains one function named as ChkNum() which accept one parameter as number.
#If number is even then it should display “Even number” otherwise display “Odd number” on console.


def ChkNum():
    no = int(input("Enter any number : "))
    c = no%2==0
    if c:
        print("Even Number")
    else :
        print("Odd Number")

ChkNum()


