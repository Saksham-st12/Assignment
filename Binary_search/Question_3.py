# Given a positive integer num, write a program that returns true if num s a perfect square else return false. Do not use built in functions like sqrt. Also talk about the time complexity of your code.


#function definition

def prfct_sqr(x):
    if x<0:
        return False 
    else:
        i ,j =1,x
        while(i<=j):
            mid= (i + j)//2
            if (mid*mid == x):
                return True
            elif( mid * mid < x):
                i = mid + 1
                    
            else:
                j = mid - 1
        return False       


#main block

x= int(input("Enter a no."))
result = prfct_sqr(x)
print(result)
