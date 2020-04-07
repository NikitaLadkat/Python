#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204


from functools import *

def fil(arr):
    brr=list()
    for x in range(0, len(arr)):
        c = even(arr[x])
        if c==True:
            brr.append(arr[x])
    return(brr)

def even(n):
    if (n%2)==0:
        return True
    else:
        return False

def square(no):
    return no**2

def red(no1,no2):
    return no1+no2



n = int(input("Enter how many number you want in list : "))
data = list()
for i in range(n):
    num=int(input("Enter the numbers : "))
    data.append(num)
print("The total data is  : ")
print(data)

print("Filtered Data is : ")
brr=fil(data)
print(brr)

print("Mapped Data is : ")
crr=list(map(square,brr))
print(crr)

ans=reduce(red,crr)
print("Ans Data is : ",ans)
