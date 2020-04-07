#Units of time

def time():
    day = int(input("Enter the no of days : "))
    h = int(input("Enter number of hours : "))
    minutes = int(input("Enter the no of minutes: "))
    sec = int(input("Enter the no of sec: "))
    d = 24*day*60*60
    print("Day_sec : ",d)
    hr = h*60
    print("Hour_Sec : ",hr)
    m=minutes*60
    print("Minutes_Sec : ",m)
    total_sec=d+hr+m+sec
    print("Total seconds : ",total_sec,"Seconds")

time()
