print("Enter the elements of the list to be sorted")
arr=list(map(int,input().split()))
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2

    l=merge_sort(arr[:mid])
    r=merge_sort(arr[mid:])

    return merge(l,r)

def merge(l,r):
    s=[]
    i=0
    j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            s.append(l[i])
            i+=1
        else:
            s.append(r[j])
            j+=1
    s.extend(l[i:])
    s.extend(r[j:])
    return s

print(merge_sort(arr))