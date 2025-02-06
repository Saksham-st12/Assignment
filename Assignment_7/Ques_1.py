# 1. Given an integer array nums of length n and an integer target, find three integers in nums
# such that the sum is closest to the target.[Amazon]
# You need to return the sum of three integers.
# For example:arr = [-1, 2, 1, -4], target = 1
# Output: 2
# Explanation: [-1+2+1] = 2 (The sum that is closest to the target is 2)




def target(nums,x):

    nums.sort()
    integers= []

    closest_sum= float('inf')
    for i in range(len(nums)-2):

        left,right = i+1,len(nums)-1
        while left<right:
            current_sum = nums[i]+nums[left]+nums[right]
            if abs(current_sum-x)<abs(closest_sum-x):
                closest_sum=current_sum
                integers= [nums[i],nums[left],nums[right]]
            
            if current_sum < x:
                left += 1
            elif current_sum> x:
                right -= 1
            else:
                break
    return integers

    



# driver code

nums=[3,1,-5,-2,6,-7,-3,-4,9,7,2]
x= 7
selected_values = target(nums,x)
print(selected_values)

# time complexity = O(n^2)
