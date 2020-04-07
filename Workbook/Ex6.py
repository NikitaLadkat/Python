#Tax and Tip

def dinner():
    meal_cost= float(input("Enter the cost of meal : "))
    tax = meal_cost*0.05
    tip = meal_cost*0.18
    gtotal=meal_cost+tax+tip
    print("Meal Cost is :", meal_cost)
    print("Tax is :", tax)
    print("Tip is :",tip)
    print("Grand total is :{}".format(gtotal))

dinner()