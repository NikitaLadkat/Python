def mean(value):
    if type(value) == dict:
        the_mean = (sum(value.values()))/(len(value))
    else :
        the_mean = (sum(value)) / (len(value))
    return the_mean


total = [1,2,3,4,5,6,7]
dicteg = {'maru': 20 , 'rita':30 , 'sita':40}

c = mean(dicteg)
d = mean(total)
print(c , d)
