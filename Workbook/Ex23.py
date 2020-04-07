#Area of regular polygon
import math

def polygon():
    s = float(input("Enter the length of side : "))
    n = float(input("Enter the number of side : "))
    pi=3.14
    area = (n*s*s)/(4*math.tan(pi/n))
    print("Area of polygon : ",area)

polygon()