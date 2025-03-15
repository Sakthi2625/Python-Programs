x=[1,2,3,4,5]

y=[i**2 for i in x]
z=[i+1 for i in x]
a=["even" if i%2==0 else "odd" for i in x]
print(a)
b=[i for i in x  if i%2==0]
print(b)
