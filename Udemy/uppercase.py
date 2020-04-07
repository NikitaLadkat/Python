def foo(*args):
    temp = []
    for x in args:
        temp.append(x.upper())
    return sorted(temp)

c = foo("lekha" , "sanket" , "rani")
print(c)