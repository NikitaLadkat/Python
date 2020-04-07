#Fuel Frequency

def fuel():
    US = float(input("Enter the Fuel in miles-per-gallon : "))
    convert = 235.215/US
    print("The Canadian Units is : ",convert,"L/100km" )


fuel()