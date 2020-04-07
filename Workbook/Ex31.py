def pressure():
    kpa = float(input("Enter the pressure in Kilopascals : "))

    pound = kpa/6.89475729
    mili = kpa*760/101.325
    mercury = kpa/101.325

    print("KPA to  Pound per Sq inch : ",pound)
    print("KPA to  milimeter of mercury : ",mili)
    print("KPA to  Atmosphere : ",mercury)


pressure()