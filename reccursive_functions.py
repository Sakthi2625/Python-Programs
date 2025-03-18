# a = int(input("Enter a number:"))

# def fact(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*fact(a-1)

# print(fact(a))

# x=[5,[2],[3,[3,4]],7,8]
# def flat(x):

#     y=[]

#     for i in x:
#         if type(i)==list:
#             y.extend(flat(i))
#         else:
#             y.append(i)
#     return y

# print(flat(x))

f=int(input("Enter the nth elements in the fibonacci series:"))

# def fibo(f):
#     h=[0,1]
#     i= 1
#     while True:
#         if f==1:
#             h.pop()
#             return h
#         elif f==2:
#             return h
#         else:
#             i = h[-2] + h[-1]
#             h.append(i)
#             if h
#     return h
        
# print(fibo(f))

def fibo(f):

    if f<=1:
        return f
    else:
        return fibo(f-1) + fibo(f-2)
    
x=[]
for i in range(f):
    x.append(fibo(i))
print(x)





            
        

   

        
