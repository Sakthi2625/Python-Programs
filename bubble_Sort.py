print("Enter the elements of the list to be sorted")
a=list(map(int,input().split()))

print("Unsorted list:",a)
p=0
swap=True
m=len(a)-1
while swap:
    swap=False
    for i in range(0,m):
        p+=1
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]  
            swap=True
            print(a)

    m-=1 
    print(swap,a)
print("Sorted List:",a,p)
