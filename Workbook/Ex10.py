#Arithematic

import math


no1=int(input("Enter the number : a : "))
no2=int(input("Enter the number : b : "))
print("a: ",no1)
print("b: ", no2)

def add():
    c= no1+no2
    print("Addition is : ",c)

def sub():
    c=no1-no2
    print("Subtraction : ",c)

def mul():
    c =no1*no2
    print("Multiplication is : ",c)

def div():
    c = no1/no2
    print("Division is : ", c)

def Remainder():
    c = no1%no2
    print("Remainder is : ", c)

def log():
    c = math.log(no1,10)
    print("Log is : ", c)

def power():
    c=no1**no2
    print("Power is : ", c)

add()
sub()
mul()
div()
Remainder()
log()
power()


