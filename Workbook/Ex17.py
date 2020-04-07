#Heat capacity


def Capacity():
    m = float(input("Enter the mass of water : "))
    t = float(input("Enter the temperature of water : "))
    c = 4.186
    price=8.9
    JtoKwh = 2.777

    q = m*c*t
    kwh = q*JtoKwh

    cost = kwh * price

    print("Total Price is  : ",cost)
    print("Total amount of energy : ", kwh)


Capacity()
