#3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5



def accept_min():
    num = int(input("Enter the numbers : "))
    arr = list()
    for i in range(0,num):
        n = int(input("Enter the num in list :"))
        arr.append(n)
    print(arr)
    print("Lowest no is  : ",min(arr))

accept_min()