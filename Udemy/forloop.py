
#Printing each letter in Capital form
for letters in 'hello':
    print(letters.title())


#If the number is of type in .
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if type(color)==int:
    #if isinstance(color, int):
        print(color)



#If the number is Int and greater than 50 :
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for x in colors:
    if type(x)==int and x>50:
        print(x)



#Dictions values need to be formated :
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for x,y in phone_numbers.items():
    print("{}: {}".format(x,y))


#replace + by 00:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for x in phone_numbers.values():
    print(x.replace("+","00"))


#