#Distance Units

def distance():
    f = float(input("Enter the value in feet : "))
    inch = f*12
    mile = f/5280
    yard = f/3
    print("Inches",inch)
    print("Miles ",mile)
    print("Yards",yard)


distance()