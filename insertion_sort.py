print("Enter the elements of the list to be sorted")
a=list(map(int,input().split()))

for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
        else:
            break
print("Sorted List:",a)