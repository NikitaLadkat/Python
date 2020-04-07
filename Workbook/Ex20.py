#Ideal gas Law

def Scuba():
    V = 12
    P = 20000000
    T = 20
    R = 8.314

    Ct = T+273.15


    n = (P*V)/(R*Ct)
    print("The Amount of gas in moles : ",n)


Scuba()