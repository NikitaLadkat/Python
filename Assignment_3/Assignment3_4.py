#4.Write a program which accept N numbers from user and store it into List.
#Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3

def frequency():
    num = int(input("Enter the numbers : "))
    arr = list()
    for i in range(0,num):
        n = int(input("Enter the num in list :"))
        arr.append(n)
    print(arr)
    p=0
    search = int(input("Enter the number to be searched : "))
    for x in (arr):
        if search==x:
            p=p+1
    print(p)


frequency()