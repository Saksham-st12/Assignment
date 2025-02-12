# Given array arr of size n,return the majority element present in the array.
# Assume that the majority element always exiist in an array

import random
def partition(arr,p,q):
    pivot_index=random.randrange(p,q+1)
    pivot = arr[pivot_index]
    arr[pivot_index],arr[p]=arr[p],arr[pivot_index]
    
    i=p

    for j in range(i+1,q+1):
        if(arr[j]<=pivot):
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[p],arr[i]=arr[i],arr[p]
    return i
def Majority(arr,p,q):

    if(p<=q):
        mid = partition(arr,p,q)
        Majority(arr,p,mid-1)
        Majority(arr,mid+1,q)
    n=len(arr)
    return arr[n//2]


#driver code
arr=[2, 2, 1, 1, 1, 2, 2]
p=0
q=len(arr)-1
result = Majority(arr,p,q)
print(result)