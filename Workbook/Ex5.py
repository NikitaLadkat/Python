#Bottle Deposit

def container():
    less=int(input("Enter the count of conrainer having less than 1 litre : "))
    more=int(input("Enter the count of conrainer having more than 1 litre : "))
    refund= (less*0.10)+(more*0.25)
    print("Refund is : ${}".format(refund))

container()