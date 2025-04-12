# problem: Left Rotate Array by K Places

# Intution: 
# if k is a multiple of length of array , then k = k % n -> such that remainder number will be our k 
# then traverse over the array and shift the elements starts from kth position to len(arr) and then insert the 
# elements from temp to the nums array

# code : 
class Solution:
    def rotateArray(self, nums, k):
        k = k % len(nums)
        temp = []
        n = len(nums)
        for i in range(k):
            temp.append(nums[i])
        for i in range(k,len(nums)):
            nums[i - k] = nums[i]
        for i in range(k):
            nums[n-k + i] = temp[i]
        return 

# TC: O(n)
# SC: O(n)
    
