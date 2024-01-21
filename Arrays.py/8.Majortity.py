# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
def f(nums):
    for i in nums:
        if nums.count(i)>len(nums)//2:
            return i

        # mx=-1
        # dic={}
        # for i in range(len(nums)):
        #     if nums[i] not in dic:
        #         dic[nums[i]]=1
        #     else:
        #         dic[nums[i]]+=1
        # mx=max(dic.values())
        # for key in dic:+
        
        #     if dic[key]==mx:
        #         return key
        
        #2nd method
    # result=0
    # count=0
    # for num in nums:
    #     if count==0:
    #         result=num
    #     if num==result:
    #         count+=1
    #     else:
    #         count-=1
    # return result
    # #3rd method using inbuilt function

    # return statistics.mode(nums)