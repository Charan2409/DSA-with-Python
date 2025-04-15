# link : https://leetcode.com/problems/contains-duplicate/description/

# Bruteforce: 
# Intuition: 
# using two nested loops to check if any number is matched twice , then return True else False
Code: 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
# TC: O(N*N)
# SC:O(1)

# Better Approach : 
# Intuition: 
# we can sort the array elements, and check the next element of the current element to see if there is a duplicate  or not 

# code : 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedList = nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: 
                return True
        return False
    
TC: O(NlogN)
SC: O(1)


# Optimal Approach: 
# using hash set , while iterating over the loop, check if the element in the hashset or not , if yes return True(seems like its already existed)
# else continue , after the loop we can return False

# code : 



