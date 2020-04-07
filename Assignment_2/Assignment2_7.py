#7. Write a program which accept one number and display below pattern.
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5


def pattern_num():
    no = int(input("Enter any number : "))
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(" ",j ,end='')
        print("\n")


pattern_num()