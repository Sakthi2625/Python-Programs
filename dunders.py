class student:
    def __init__(self,count):
        self.count=count
    def __iter__(self):
        return self
    def __next__(self):
        value=self.count
        self.count-=1
        if value<0:
            raise StopIteration
        return value

s=student(5)
for i in s:
    print(i)
