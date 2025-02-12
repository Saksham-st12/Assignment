# Given an array nums and an integer k,return the kth largest no

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
def Quick_sort(arr,p,q):

    if(p<=q):
        mid = partition(arr,p,q)
        Quick_sort(arr,p,mid-1)
        Quick_sort(arr,mid+1,q)
    return arr
def kth_element(arr,p,q,k):
    sorted_arr=Quick_sort(arr,p,q)
    k_largest=sorted_arr[len(arr)-k]
    return k_largest


#driver code
arr= [40,25,68,79,52,66,89,97]
p,q=0,len(arr)-1
k=2
result=kth_element(arr,p,q,k)
print(result)


