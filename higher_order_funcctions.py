# w=[{"Name":"Speaker","Rate":500},{"Name":"Soap","Rate":50},{"Name":"Rice","Rate":80}]

# y=list(map(lambda x: {"Name":x["Name"],"Rate":x["Rate"]-(x["Rate"]*0.25)} if x["Rate"]>100 else x, w))

# print(y)

# x=list(map(lambda x: x**2,[i for i in range(7)]))
# print(x)

# s=[180,130,150,140,170]

# b=list(map(lambda i: "L" if i>160 else "M" if 140<i<160 else "S",s))

# print(b)

# a=[7,8,9,10]

# l=list(filter(lambda x: x%2==0,a))

# print(l)

f=["apple","banana","mango","manga"]

a_f=list(filter(lambda h: h.count("a")>1 ,f))
print(a_f)
# c="a"
# for i in f:
#     # print(i)
#     if i.count(c)>1:
#         print(i)


    







