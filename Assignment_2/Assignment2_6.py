#Write a program which accept one number and display below pattern.
#Input : 5
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

def pattern2():
    no = int(input("Enter any number : "))

    for i in range(no,0,-1):
        for j in range(1,i+1):
            print("*",end=' ')
        print("\n")

pattern2()