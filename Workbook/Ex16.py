#Area and  volume

def area():
    a = pi*r*r
    print("Area of circle is :", a)

def sphere():
    v = 1.333*pi*r*r*r
    print("Volume of sphere is : ",v)

r = float(input("Enter the radius : "))
pi = 3.14
area()
sphere()