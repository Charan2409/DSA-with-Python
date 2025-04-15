# problem: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

# Intuition: 
# 1.we will have one variable to track zero element as index and used for swapping for non zero element
# 2.we will iterate over the array or list , and then if we find any then we can swap non zero element with element at nums[variable] and increment the variable count by 1
# to move to next element[since we have a check to find non zero ,so this variable always holds the zero element]

# Code: 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insertIndex], nums[i] = nums[i], nums[insertIndex]
                insertIndex += 1
        return
    
# TC: O(n)
# sc: O(1)
