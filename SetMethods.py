# #add
# s={5,1,3,2}
# s.add(7)
# print(s)
# #Remove
# s.remove(7)
# print(s)
# #Discard
# s.discard(5)
# print(s)
# #pop
# r=s.pop()
# print(r)
# #clear
# s.clear()
# print(s)


# #Set Operations
# s1={1,2,4}
# s2={4,5,6}
# #Union
# s=s1.union(s2)
# print(s)
# #Intersection
# s=s1.intersection(s2)
# print(s)
# #Difference
# s=s1.difference(s2)
# print(s)
# #Update
# s1.update(s2)
# print(s1)
# #Intersection update
# s1.intersection_update(s2)
# print(s1)
# #Difference update
# s1.difference_update(s2)
# print(s1)
# s1={1,2,4}
# s2={4,5,6}
# #Symmetric Difference
# s=s1.symmetric_difference(s2)
# print(s)
# #Symmetric Difference Update
# s1.symmetric_difference_update(s2)
# print(s1)
# #issubset
# s1={1,2}
# s2={1,2,3,4}
# r=s1.issubset(s2)
# print(r)
# #issuperset
# r=s1.issuperset(s2)
# print(r)
# #isdisjoint
# r=s1.isdisjoint(s2)
# print(r)

a={1,2,3,4,5,6,7,5}
b={5,6,7,8,9,10,11}
c=set()

# for i in a:
#     for j in b:
#         if i==j:
#             c.add(i)
# print(c)

for i  in a:
    if i in b:
        c.add(i)
print(c)

