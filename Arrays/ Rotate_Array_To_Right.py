# problem:  Rotate Array

# Leetcode link : https://leetcode.com/problems/rotate-array/description/

# Intuition:
# if k is a multiple of length of array , then k = k % n -> such that remainder number will be our k 
# then traverse over the array and shift the elements starts from kth position to left and then insert the 
# elements from temp to the nums array [ ] from end side or right side

# Code:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = []
        for i in range(n-k, n):
            temp.append(nums[i])
        for i in range(n-1, -1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = temp[i]
        return 
    
# TC: O(N)
# SC: O(N)