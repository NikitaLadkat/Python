#Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input : 4 Output : 16
#Input : 6 Output : 64

no=int(input("Enter the number : "))
fptr = lambda no: 2**no
print(fptr(no))
