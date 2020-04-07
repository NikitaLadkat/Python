#Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56


def accept_max():
    num = int(input("Enter the numbers : "))
    arr = list()
    for i in range(0,num):
        n = int(input("Enter the num in list :"))
        arr.append(n)
    print(arr)
    print("Highest no is  : ", max(arr))

accept_max()
