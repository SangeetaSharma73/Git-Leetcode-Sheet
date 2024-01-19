# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# T.c=O(n)
nums = [0,1,0,3,12]
i=0
for j in range(len(nums)):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
print(nums)
