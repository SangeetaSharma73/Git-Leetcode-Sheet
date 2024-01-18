# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
arr=[2,7,11,15]
taget=9
def fun(arr,target):
    #using brute force-T.c=O(n^2)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]

#using dictionary-T.c=O(n) and S.c=O(n)
nums=[5,4,8,2]
target=6
def fun(arr,target):
    dict={}
    for i in range(len(nums)):
        req=target-nums[i]
        if req in dict:
            return [dict[req],i]
        dict[nums[i]]=i