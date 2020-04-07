class cat:

    def __init__(self,name):
        self.name = name
        print("name of cat is : "+ self.name)

    def sit(self):
        print("the cat "+self.name+" is sitting")


mycat = cat('sweety')
print(mycat.sit())