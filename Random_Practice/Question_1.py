# Challenge 1: The "Two Sum" Problem
# This is a classic interview question and great for practicing your problem-solving skills. Here’s the task:

# Problem: You are given an array of integers and a target value. You need to find two numbers in the array such that their sum equals the target value.

# Write a function that takes in an array nums and a target x, and returns the indices of the two numbers that add up to the target.

def target(arr,x):
    arr.sort()
    num_1_2 = []
    for i in range(len(arr)):
        left=i
        right=len(arr)-1
        while left<right:
            if arr[left]+arr[right] == x:
                num_1_2.append([arr[left],arr[right]])

            if arr[left] + arr[right] <x:
                left += 1
            elif arr[left] + arr[right] >x:
                right -= 1
            else:
                break
    return num_1_2
    return left, right

arr=[2,1,3,4,2]
x=4
result = target(arr,x)
print(result)
