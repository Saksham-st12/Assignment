# 2. Given three points, check whether they lie on a straight (collinear) or not. [Google]
# For example:
# Input- [(1,1), (1,6), (0,9)]
# Output- No
# Input- [(1,1), (1,4), (1,5)]
# Output- Yes


def is_collinear(arr):
    x,y = list(zip(*arr))
    x1,x2,x3 = x
    y1,y2,y3 = y
    area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))//2
    if area==0:
        return "Yes"
    else:
        return "No"



#driver code
arr =[(1,1), (1,4), (1,5)]

result =is_collinear(arr)
print(result)
