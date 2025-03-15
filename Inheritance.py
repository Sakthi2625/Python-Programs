# class Father:
#     def showMyName(self):
#         print("AAAAAA")
# class child(Father):
#     pass
# o=child()
# o.showMyName()

class Parent:
    def showMyName(self):
        print(self.name)
    def __init__(self,name):
        self.name=name

class child(Parent):
    pass

o=child("Esakki")
o.showMyName()