# problem : 1071. Greatest Common Divisor of Strings
# Leetcode link : https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
# Intuition: 
#  -> if concatenated strings of both str1 and str2 is not identical when we do str1 + str2 == str2 + str1, 
# then we can conclude that there is a common longest substring which makes string1 and string2,

#So that's why we use greatest common divisor technique on both length of strings to find largest divisor which forms both strings

# Code: 
from collections import list
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: 
            return ""
        size = math.gcd(len(str1), len(str2))
        return str1[:size]
    
# TC: (len(str1) + len(str2))

