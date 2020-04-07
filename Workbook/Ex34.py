#Day old Bread


def bread():
    no = int(input("Enter the no if bread loaves : "))
    new = no*3.49
    old = new*0.60
    dis= new-old
    print("Regular = ",new)
    print("Dicounted amount = %.2f",format(dis))
    print("Total of old Bread = ",old)


bread()
