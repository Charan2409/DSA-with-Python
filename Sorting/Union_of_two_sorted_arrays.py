# problem (TUF's problem) : 
# Union of two sorted arrays
# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.

# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

# Examples:
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
# Output: [1, 2, 3, 4, 5, 7]
# Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2
# Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
# Output: [1, 3, 4, 5, 6, 7, 8, 9]
# Explanation: The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2

# BruteForce: 
# Intuition:
# iterate over each arrays and append to new set[to remove difficulties] and iterate over set and add those elements
# into a list, and sort the list

# Code: 
class Solution:
    def unionArray(self, nums1, nums2):
        newset = set()
        newarray = []
        for i in range(len(nums1)):
            newset.add(nums1[i])
        for i in range(len(nums2)):
            newset.add(nums2[i])
        for num in newset:
            newarray.append(num)
        newarray.sort()
        return newarray
# TC: (m + n + (m*n logn))
# sc: m+n

# Optimal Code: 
# Intuition: 
# take one sortedArray to store the elements, use two pointer technique parallelly on two arrays ,
# if i < m and j < n (so it means we are in middle of comparing, then we compare the smallest element from both lists and 
# and check if its already existed in sortedArray or not , if not append the element to sortedArray,
# if any iteration is incomplete, then check if element is not inside sortedArray, then appendit 

# Code: 
class Solution:
    def unionArray(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        sortedArray = []
        i = 0
        j = 0
        while (i < m and j < n):
            if nums1[i] <= nums2[j]:
                if nums1[i] not in sortedArray:
                    sortedArray.append(nums1[i])
                i += 1
            else:
                if nums2[j] not in sortedArray:
                    sortedArray.append(nums2[j])
                j += 1
        while i < m:
                if nums1[i] not in sortedArray:
                    sortedArray.append(nums1[i])
                i += 1
        while j < n:
            if nums2[j] not in sortedArray:
                sortedArray.append(nums2[j])
            j += 1
        return sortedArray

# TC : O(m * n)
# sc: O(m + n)
