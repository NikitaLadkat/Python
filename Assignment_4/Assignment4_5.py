#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all prime numbers.
# Map function will multiply each number by 2.
# Reduce will return Maximum number from that numbers.
#(You can also use normal functions instead of lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62

from functools import *

def fil(arr):
    brr=list()
    for x in range(0,len(arr)):
        p = prime(arr[x])
        if p==False:
            brr.append(arr[x])
    return brr


def prime(num):
    if num>1:
        for i in (2,num):
            if num!=2 and (num%i)==0:
                return True
            elif num==1:
                return True
            else:
                return False



def modify(num):
    return num*2

def maximum_num(no1,no2):
      return max(no1,no2)


n = int(input("Enter how many number you want in the list : "))
data=list()
for i in range(0,n):
    num = int(input("Enter the number : "))
    data.append(num)
print("The List of all numbers : ")
print(data)

print("Filtered Data is : ")
brr=fil(data)
print(brr)

print("Mapped Data is : ")
crr=list(map(modify,brr))
print(crr)

#ans=max(crr)
ans=reduce(maximum_num,crr)
print("Answer is : ",ans)