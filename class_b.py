import class_a

class B:
    def __init__(self):
        pass
    def getName(self):
        print("B")
    def getAllData(self,data):
        self.data=data

b=B()
a=class_a.A()
b.getName()
a.getName()
# class_a.A.getName()
print(__name__)
