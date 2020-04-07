#Distance between two points on earth

import math


def Distance():
    t1 = float(input("Enter point-1 t1: "))
    g1 = float(input("Enter point-1 g1: "))
    t2 = float(input("Enter point-2 t2: "))
    g2 = float(input("Enter point-2 g2: "))
    dist = 6371.01*(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    print("Distance is : " ,dist)


Distance()