def weather(temp):
    if temp <= 10 :
        return "Cold"
    else:
        return "Warm"


c = float(input("Enter the temp"))
print(weather(c))
