# problem name : 20. Valid Parentheses

# Leetcode Link : https://leetcode.com/problems/valid-parentheses/description/

# Intuition: 
# for open bracket , we can store in stack and check the next element if its closing bracket, then take out 
# take out the element from stack and validate if both are open and closing brackets , then proceed to next 
# element and also check if the stack is empty for a current element is closing bracket , then return false [edge case , since 
# no open bracket for it] , at end of string iteration also check if stack is empty or not , if its not, then 
# return False else return True

# Code: 

class Solution:
    def isValid(self, s: str) -> bool:
        openingBrackets = ["{", "[", "("]
        stack = []
        for i in range(len(s)):
            if s[i] in openingBrackets:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                q = stack.pop()
                if s[i] == "]" and q != "[" or s[i] == "}" and q != "{" or s[i] == ")" and q != "(":
                    return False
        if len(stack) != 0:
            return False
        return True

# TC: O(N)
# SC : O(N)

