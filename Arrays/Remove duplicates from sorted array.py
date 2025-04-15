# leetcode link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Intuition: 

# BruteForce:
# we can create and add the elements in a set(which will have unique elements only), and replace the elements from sorted list of set with nums array list from Start

# Code: 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newSet = set()
        for i in range(len(nums)):
            newSet.add(nums[i])
        sortedList = sorted(newSet)
        for i in range(len(sortedList)):
            nums[i] = sortedList[i]
        return len(sortedList)
    
# TC:O(NlogN)
# SC: O(N)


# Optimal Approach:
# Intuition : 
# we can use two pointer , one pointer is at 0 index position , and iterate from 1 index to check, if its a different element to pointer position
# element,  then put that element beside right to the pointer position element and increment pointer to fill the unique elements and return pointer + 1 as a count


# code: 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != nums[pointer]:
                nums[pointer + 1] = nums[i]
                pointer += 1
        return pointer+1
    
# TC: O(N)
# SC: O(1)

