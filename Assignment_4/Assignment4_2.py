#Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18

no1=int(input("Enter the number no1 : "))
no2=int(input("Enter the number no2 : "))
fptr = lambda no1,no2: no1*no2
print (fptr(no1,no2))
