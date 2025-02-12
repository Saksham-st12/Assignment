# The peak element is thge element that is strictly greater than its neighbor.if an array contains multiple peak elements, return the index of any 0f the peak elements

import random
def peak(arr):
    peak_index=[]
    for i in range(1,len(arr)-1):
        if(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
            peak_index.append(i)
    c=random.choice(peak_index)
    return c

#driver code
arr= [1, 3, 2, 4, 1, 6, 5, 7, 3]
result=peak(arr)
print(result)