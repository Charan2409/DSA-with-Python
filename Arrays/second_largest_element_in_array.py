# we have to find the second largest element in array 

# Brute Force approach: 
# We can sort the list or array and then we can traverse the list from second element in reverse order 
# and check if current element is not the largest , then we can return it as  the second largest

# code:

class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        if n <2:
            return -1
        nums.sort()
        maximum = nums[-1]
        second_largest = -1
        for i in range(n-2, -1, -1):
            if nums[i] != maximum:
                second_largest = nums[i]
                break
        return second_largest

# TC: O(NlogN)

# better approach : 
#we will not use sort function or sorting [to reduce logn complexity] and find the largest and smallest 
# using largest = nums[0] and secondLargest = float('-int') -> its the smallest number possible or -infinity
# code: 
class Solution:
    def secondLargestElement(self, nums):
        # Get the length of the array
        n = len(nums)

        # Check if the array has less than 2 elements
        if n < 2:
            # If true, return -1 indicating there is no second largest element
            return -1 

        # Initialize variables to store the largest and second largest elements
        largest = nums[0]
        secondLargest = -1

        # First traversal to find the largest element
        for i in range(n):
            largest = max(largest, nums[i])

        # Second traversal to find second largest element
        for i in range(n):
            if nums[i] > secondLargest and nums[i] != largest:
                secondLargest = nums[i]

        # Return the second largest element
        return -1 if secondLargest == -1 else secondLargest
    
    # TC: O(2N)

#Optimal Approach : 

#intuition: we will use two variables starts from two edges and compare the largest and if its greater than second largest and not equal to the largest , 
# return it

class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 2:
            return -1
        largest = nums[0]
        secondLargest = float('-inf')
        for i in range(len(nums)):
            if nums[i] > largest: 
                secondLargest = largest
                largest = nums[i]
            elif nums[i] > secondLargest and nums[i] != largest:
                secondLargest = nums[i]
        return -1 if secondLargest == float('-inf') else secondLargest
    
# TC: O(N)


    