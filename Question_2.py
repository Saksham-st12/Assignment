# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous versions, all the versions after a bad version are also bad. Suppose you have n version and you want to find out the first bad one, which causes all the following ones to be bad. Also, talk about the time complexity of your code.



def bad(arr,x):
    for i in range (0 , len(arr)):
        if(arr[i] == x):
            return ('The first error is present at index no:',i)
        else:
            i = i+1
    
    i, j = 0, len(arr )-1
    result = -1

    while (i<= j):
        mid = (i+(j-i)//2)
        if(arr[mid] == x):
            result = mid
            j= mid -1
        else:
            (arr[mid] < x)
            i = mid+1
            
            
    return result


arr =[ 1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = 0
i =0
j = len(arr)-1
mid = i + (j-i)/2
result = bad(arr,x)
print(result)
