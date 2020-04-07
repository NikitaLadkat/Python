def pattern():
    no = int(input("Enter any number : "))
    for i in range(1, no+1):
        for j in range(1, no+1):
            print(" * ", end='')
        print("\n")


pattern()
