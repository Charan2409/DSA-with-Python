# problem : Maximum Consecutive Ones

# Intuition: 
# we will maintain count and maxCount variables to track the consecutive ones, and in the iteration if the number
# is 1 then we will increase the count and check if count is greater than the maxCount , then give the max value to
# maxCount variable and at the end return the maxCount

# Code - optimal solution: 

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0
        return maxCount
        
# TC: O(n)
# SC: O(1)