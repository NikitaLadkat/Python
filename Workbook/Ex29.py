#Wind Chill

def wind():
    temp = float(input("Enter the Temperature : "))
    V = float(input("Enter the Speed : "))
    WCI = 13.12 + 0.6215*temp**0.16-11.3*V**0.16+0.3965*temp*V**0.16
    print("Wind Chill is : ",int(WCI))

wind()