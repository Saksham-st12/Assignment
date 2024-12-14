
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.And since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned. Also, talk about the time complexity of your code.


def sqr_root(x):

    if(x>0):
        i ,j =1,x
        while(i<=j):
            mid= (i + j)//2
            if (mid*mid == x):
                return int(mid)
            elif( mid * mid < x):
                i = mid + 1
                
            else:
                j = mid - 1
        return int(mid)       

    elif(x==0):
        return "Sqr root of 0 is 0"
    else:
        return 0


x = int(input("Enter a number: "))
result = sqr_root(x) 
print(result)   