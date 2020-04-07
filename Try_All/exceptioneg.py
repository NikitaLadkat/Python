message = ("How many tickets do you want..")
num_tickets = input(message)


try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Try Again")
else:
    print("Successful")