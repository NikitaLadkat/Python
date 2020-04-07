#Write a program which accept one number form user and return addition of its factors.


def factor():
    no = int(input("Enter any number : "))
    result=0
    for i in range(1,no):
        if no%i==0:
            result=result+i

    print(result)




factor()

