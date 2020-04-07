#Free fall

import math

def free():
    h = float(input("Enter the height : "))
    a = 9.8
    s = 0
    vf = math.sqrt(s*s+2*9.8*h)
    print("Free fall is : ", vf)


free()