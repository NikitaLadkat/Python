
#password length
def foo(value):
    if len(value) >= 8:
        return True
    else:
        return False
foo("mylongpass")




#Temp
def tempt(temp):
    if temp <= 7:
        return "cold"
    else:
        return "warm"

tempt(9)