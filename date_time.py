from datetime import datetime
# print(datetime.now())

x=datetime.now()
# print(x.strftime("%Y"))
# print(x.strftime("%m"))
# print(x.strftime("%d"))
# print(x.strftime("%H"))
# print(x.strftime("%M"))
# print(x.strftime("%S"))
# print(x.strftime("%a"))
y=datetime(2024,10,16)
z=x-y
print(z)
print(z.days)
print(z.seconds)
hours=z.seconds//3600
minutes=(z.seconds%3600)//60
print(hours)
print(minutes)
