#Area of triangle (Again)

import math

def area():
    s1 = float(input("Enter the Side one : "))
    s2 = float(input("Enter the Side two : "))
    s3 = float(input("Enter the Side three : "))
    s= (s1+s2+s3)/2
    a = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("Area of Triangle using side is : ",a)


area()
