# problem : 238. Product of Array Except Self

# Leetcode link: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# code: 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(len(nums)-1, 0, -1):
            output.append(output[-1]*nums[i]) #creating output or right array 
        output = output[::-1] #reversing the right array based on index from left
        left = 1
        print(output)
        for i in range(len(nums)):
            output[i] *= left #multiplying every element of output with left [which will be the product of previous elements of i or current iterator]
            left *= nums[i]
        return output
    
# TC: O(n)
# Space complexity: O(1)