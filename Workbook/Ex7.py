#Sum of first n  positive numbers

def sum_integer():
    n = int(input("Enter any positive number : "))
    sum = (n*(n+1))/2
    print("The Sum of 1 to n integers is : ",sum)
sum_integer()