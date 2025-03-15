# x=[7,8,9]
# print(x)
# #Append
# x.append(10)
# print(x)
# #Extend
# x.extend([1,2])
# print(x)
# #Insert
# x.insert(2,33)
# print(x)
# #Update
# x[2]=40
# print(x)
# #update2
# x[1:3]=[5,5]
# print(x)
# #Removing an element in a List
# x.remove(5)
# print(x)
# x.pop(4)
# print(x)
# x.pop()
# print(x)
# #Clear
# x.clear()
# print(x)
# #Copy
# x=[7,8,9,8,18,8,9]
# y=x.copy()
# print(y)
# #Sort
# x.sort()
# print(x)
# #Sort in descending order
# x.sort(reverse=True)
# print(x)
# #Reverse Function
# x.reverse()
# print(x)
# #Reverse2
# z=x[::-1]
# print(z)
# #Reverse3
# x[:]=x[::-1]
# print(x)
# #Index Function
# x=[7,8,9,8,18,8,9]
# u=x.index(8)
# print(u)
# q=x.index(8,4,7)
# # print(q)
# # #Count
# # t=x.count(8)
# # print(t)

# s=[7,8,9,7,12,14,7,13,7]
# # i=0
# # while 7 in s[i:]:
# #     a=s.index(7,i)
# #     print(a)
# #     i=a+1

# #Alternative Method:
# a=-1
# b=7
# for i in range(s.count(b)):
#     v=s.index(b,a+1)
#     print(v)
#     a=v

# x=[7,8,9,2,3,4]
# y=[]
# j=len(x)-1
# for r in range(len(x)):
#     if r<=(len(x)-1):
#         y.append(None)/
# for i in x:
#     y[j]=i
#     j-=1
# print(y)

# x = [7, 8, 9, 2, 3, 4]
# y = []

# for i in range(len(x) - 1, -1, -1):
#     y.append(x[i])
# print(y)

# a=[7,8,9,10,11,12]
# b=a.copy()
# j=len(a)-1

# for i in range(len(a)):
#     if i<(round(len(a)/2)):
#         a[i]=a[j]
#     else:
#         a[i]=b[j]
#     j-=1
# print(a)

# a=[7,8,9,10,11,12,13,14,15]
# # b=a.copy()
# x=len(a)-1
# for i in range(len(a)):
#     a[i]=b[x-i]
# print(a)
 
# for i in range(len(a)):

#     a[i],a[x]=a[x],a[i]
#     x-=i
# print(a)
# a = [7, 8, 9, 10, 11, 12,13]
# n = len(a)

# for i in range(n // 2):
#     a[i], a[n - i - 1] = a[n - i - 1], a[i]

# print(a)

# x=[5,6,7,1,2,3,4]
# i=int(input("Element to be in first:"))
# j=x.index(i)
# # y=x.pop(j)
# # x.insert(0,y)
# # print(x)
# for j in range(len(x)):
#     if x[j]==i:
#         x[0],x[j]=x[j],x[0]
        
# print(x)
# x.remove(i)
# y=[i]
# for j in range(len(x)):
#     if x[j]!=i:
#         y.append(x[j])
# print(y)

# x=[5,6,7,1,2,3,4]
# y=x.copy()
# i=int(input("Element to be in first:"))
# j=x.index(i)
# for r in range(0,j+1):
#     if r!=j:
#         x[r+1]=y[r]
# x[0]=i
# print(x)

a=[7,8,9,10,1,12,13,15,2]
y=a.copy()
i=int(input("Element to be in first:"))
f=int(input("2nd Element:"))
j=a.index(i)
m=a.index(f)
# for r in range(m+1):
#     if r==0:
#             a[r]=y[j]
#     elif r==(j+1):
#             a[r]=y[m]
#     elif r<=m:
#         a[r]=y[r-1]
# print(a)

for r in range(m+1):
    if y[r]==1:
        a[0]=1
    elif y[r]==2:
        a[j+1]=2
    else:
        a[r+1]=y[r]
print(a)