#Sum of the Digits in an Integer

def sum():
    no = int(input("Enter the number : "))
    print("The Number entered is : ",no)
    total = 0
    rem = 0
    while no>0:
        rem = no % 10
        total = total + rem
        no //= 10
        print(rem)
    print("Sum is : ", total)

sum()