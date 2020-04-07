myfile = open("job.txt")
c = myfile.read()
myfile.close()
print(c[:10])
