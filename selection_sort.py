print("Enter the elements of the list to be sorted")
a=list(map(int,input().split()))

def selection_sort(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]

s= selection_sort(a)
print("Sorted List:",a)