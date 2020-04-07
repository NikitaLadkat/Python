#WAP which accept N numbers from user and store it into List. Return addition of all elements from that List.

def list_take():
    total=0
    num = int(input("Enter how many numbers you want :"))
    li=list()
    for i in range(0,num):
        n = int(input("Enter num :"))
        li.append(n)
    print("Entered list is : " ,li)
    for i in range(0,num+1):
        total=total+i
    print(total)


list_take()