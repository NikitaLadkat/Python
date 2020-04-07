def ChkPrime(num):
    if num>1:
        for i in (2,num):
            if num!=2 and (num%i)==0:
                return True
            elif num==1:
                return True
            else:
                return False



def add(no):
    ad=0
    for i in range(0, len(no)):

        ad=ad+no[i]
    return ad