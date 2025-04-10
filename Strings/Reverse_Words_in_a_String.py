# 151. Reverse Words in a String

# leetcode link : https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# brute force approach : 
class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split()
        res = []
        i = len(lis) - 1
        while i>= 0:
            res.append(lis[i])
            i -= 1
        return " ".join(res)
    
# TC: O(n + m) -> n is the length of string, m is the words to reverse

# Optimal approach: 

# code: 

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
# TC: O(n)

