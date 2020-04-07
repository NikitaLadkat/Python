#Compound Intrest

def saving():
    amt = float(input("Enter the monthly amount deposited : "))
    year=amt*12
    yearly = year+ year*0.04
    sec_year = yearly + yearly*0.04
    thrd_year = sec_year+ sec_year*0.04
    print("Total amount Monthly : %.2f" % amt)
    print("Total amount Yearly : %.2f" %year)
    print("Total Savings amount including interst for 1 year : %.2f" %yearly)
    print("Total Savings amount including interst for 2 years : %.2f" %sec_year)
    print("Total Savings amount including interst for 3 years : %.2f" %thrd_year)

saving()
