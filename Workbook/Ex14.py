#Height Units

def height():
    f = float(input("Enter te height in feet : "))
    i = float(input("Enter the inches if more than 1 else write zero : "))
    height_calc=f*12
    hc=height_calc*2.54
    print("Hight is {} cm".format(hc))

height()