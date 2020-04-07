#Units of Time (Again)

def sec_returns():
    t_sec = int(input("Enter the time in seconds : "))
    day = t_sec/86400
    print("Day  : ",round(day))
    c = t_sec%86400
    hr = c/3600
    print("Hr : ",int(hr))
    p =  c%3600
    min = p/60
    print("Min : ",int(min))
    q = p%60
    print("Sec is : " , int(q))
    print("Format: \nD : HH : MM : SS")
    print(round(day),":",int(hr),":",int(min),":",(q))

sec_returns()