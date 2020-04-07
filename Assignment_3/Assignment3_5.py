#5.Write a program which accept N numbers from user and store it into List.
#Return addition of all prime numbers from that List.
#Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum.
# Name of the function from main python file should be ListPrime().
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output : 54 (13 + 5 + 7 +2 + 5)

from Assignment_4 import MarvellousNum


def ListPrime(arr):
    a=list()
    for x in range(0,len(arr)):
        n= MarvellousNum.ChkPrime(arr[x])
        if n==False:
            a.append(arr[x])
    return a

n = int(input("Enter how many nos : "))
data = list()
for i in range(n):
    num = int(input("Enter the number : "))
    data.append(num)
print(data)

y =ListPrime(data)
print("Prime is :")
print(y)

ans= MarvellousNum.add(y)
print("Ans : ", ans)