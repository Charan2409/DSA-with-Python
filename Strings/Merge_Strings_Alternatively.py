#link : https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
# problem number : 1768. Merge Strings Alternately
# Intuition : add pointers on each string and add alternate characters from each string into a result list 
#and check for the string length with pointers or pointer [if its exceeded or not ], if exceeded add the substring from last pointed index to the last inthe long string or 
# we can traverse the strings using single pointer and add alternate char from strings into result list
#and increment the pointer to move further by 1 

# Solution 1 : 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        m = len(word1)
        n = len(word2)
        i, j = 0, 0
        while i < m or j < n:
            if i < m: 
                res.append(word1[i])
                i += 1
            if j < n: 
                res.append(word2[j])
                j += 1

        return "".join(res)

#solution 2: 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        m = len(word1)
        n = len(word2)
        i, j = 0, 0
        while i < m and j < n:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)

#TC: O(m+n)
            
        

