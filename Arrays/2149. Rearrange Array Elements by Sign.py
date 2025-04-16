# leetcode: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
# Problem is there in TUF & leetcode

# Brute Force :
# code
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = []
        negative = []
        res = []
        for i in range(n):
            if nums[i] >= 0:
                positive.append(nums[i])
            else: 
                negative.append(nums[i])
        for i in range(n // 2):
            res.append(positive[i])
            res.append(negative[i])
        return res
    
# TC : O(2N)
# SC: (2N)

# Optimal : 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        posIndex = 0
        negIndex = 1
        for i in range(n):
            if nums[i] < 0:
                res[negIndex] = nums[i]
                negIndex += 2
            else:
                res[posIndex] = nums[i]
                posIndex += 2
        return res
        
# TC :O(n)
# SC: O(n)