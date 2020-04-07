#Write a program which accept number from user and return addition of digits in that number.



def total_Sum():
    num = int(input("Enter any long number : "))
    rem=0
    total=0
    while num>0 :
        rem = num%10
        total=total+rem
        num//=10
    print(total)

total_Sum( )