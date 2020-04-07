import time

while True:
    with open("vegis.txt") as f1:
        c = f1.read()
        print(c)
        time.sleep(5)
