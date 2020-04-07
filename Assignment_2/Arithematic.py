def Add():
    no1 = input("Enter the 1st number : ")
    no2 = input("Enter the 2st number : ")
    c =  int(no1)+int(no2)
    print(c)

def Sub():
        no1 = input("Enter the 1st number : ")
        no2 = input("Enter the 2st number : ")
        c = int(no1) - int(no2)
        print(c)

def Mul():
    no1 = input("Enter the 1st number : ")
    no2 = input("Enter the 2st number : ")
    c =  int(no1)* int(no2)
    print(c)

def Div():
        no1 = input("Enter the 1st number : ")
        no2 = input("Enter the 2st number : ")
        if no1<no2:
            c = int(no1) / int(no2)
            print(c)
        else:
            print("Please give valid input !! ")