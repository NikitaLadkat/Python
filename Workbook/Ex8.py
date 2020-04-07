#Widgets and Gizmos

def retailer():
    w = int(input("Enter the number of Widgets : "))
    g = int(input("Enter the number of Gizmo : "))
    total = w*75 + g*112
    print("Total weights is {} grams".format(total))

retailer()