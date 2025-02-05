
# Using ternary search check if the number entered by user is present in the array or not and if it is present then give the index of the number.



def ternarySearch(arr, i, j, key):


    while i <=j:
        mid1 = i+(j-i)//3
        mid2 = j-(j-i)//3
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif arr[mid1] > key:
            return ternarySearch(arr,i,mid1-1,key)
        
        elif arr[mid2] < key:
            return ternarySearch(arr,mid2+1,j,key)
        else:
            return ternarySearch(arr,mid1 +1,mid2-1,key)
    return -1
        



arr = [ 20, 25, 47, 56, 59, 63, 65, 79, 82]
x= int(input("Enter the number: "))
i,j =0,len(arr)-1
result = ternarySearch(arr,i,j,x)

# Using ternary search check if the number entered by user is present in the array or not and if it is present then give the index of the number.



def ternarySearch(arr, i, j, key):


    while i <=j:
        mid1 = i+(j-i)//3
        mid2 = j-(j-i)//3
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif arr[mid1] > key:
            return ternarySearch(arr,i,mid1-1,key)
        
        elif arr[mid2] < key:
            return ternarySearch(arr,mid2+1,j,key)
        else:
            return ternarySearch(arr,mid1 +1,mid2-1,key)
    return -1
        



arr = [ 20, 25, 47, 56, 59, 63, 65, 79, 82]
x= int(input("Enter the number: "))
i,j =0,len(arr)-1
result = ternarySearch(arr,i,j,x)

print(result)