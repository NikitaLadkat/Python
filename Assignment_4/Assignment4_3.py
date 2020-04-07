#3.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that numbers.
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000


from functools import *

def fil(arr):
    brr = list()
    for i in range(0,len(arr)):
        n=greater(arr[i])
        if n==True:
            brr.append(arr[i])
    return brr


def greater(no):
    if no>=70 and no<=90:
        return True
    else:
        return False

def modify(n):
   return n+10


def red(n1,n2):
    return n1*n2

no = int(input("Enter how many numbers in a list : "))
arr = list()
for i in range(no):
    n = int(input("Enter the number : "))
    arr.append(n)
print("Arr is : ")
print(arr)

print("Filtered data is : ")
brr = fil(arr)
print(brr)
crr =list(map(modify,brr))
print("Mapped data is : ")
print(crr)
ans=reduce(red,crr)
print("Answer is : ", ans)

