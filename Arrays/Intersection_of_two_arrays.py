# leetcode : https://leetcode.com/problems/intersection-of-two-arrays/description/

# Intuition: 
# Keep visited array for the second array and traverse on both arrays nested to check if the elements are matched , then we can add the elements 
# to result array. at last if any element is greater than element in break the inner loop 

Code: 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        vis = [0] * len(nums2)
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and vis[j] == 0:
                    if nums1[i] not in res:
                        res.append(nums1[i])
                        vis[j] = 1
                        break
        return res
    
# TC: O(m *n)
# sc: (m + n)

# OptimaL :
# using hashset to add the second array elements and then iterate over first array and check the current element is there or not in set , if there 
# add it the result array and remove it from set , and return the result

# code: 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        newset = set()
        m = len(nums1)
        n = len(nums2)
        for i in range(n):
            newset.add(nums2[i])
        for i in range(m):
            if nums1[i] in newset:
                res.append(nums1[i])
                newset.remove(nums1[i])
        return res

# TC: O(m + n)
# space - complexity: O(n)



