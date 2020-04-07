#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add():
    no1= input("Enter 1st no : ")
    no2 = input("Enter 2st no : ")
    a = int(no1)+int(no2)
    return(a)

c = Add()
print("Addition is : ",c)