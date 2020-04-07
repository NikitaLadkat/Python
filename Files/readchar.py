def l(x , filepath="job.txt"):
    file = open(filepath)
    c = file.read()
    return c.count(x)

z = l("e")
print(z)