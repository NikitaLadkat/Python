#Sort 3 Integer

def sort():
    no1= int(input("Enter the number 1 : : "))
    no2= int(input("Enter the number 2 : : "))
    no3= int(input("Enter the number 3 : : "))
    c= max(no1,no2,no3)
    d= min(no1,no2,no3)
    print("Maximum : ",c)
    print("Minimum : ",d)
    middle=(no1+no2+no3)-c-d
    print("Middle value : ",middle)

sort()