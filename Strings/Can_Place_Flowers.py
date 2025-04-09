# Problem : Can Place Flowers

# Leetcode link: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

# Intuition: 
# traverse the flowerbed to see any specific index has 0 as element and adjacent elements should also be 0 , then we can place 1 over there and decrease the n value by one
# consider the left adjacent to first elememt is 0 by default and right adjacent to the last element is 0 

# code:

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            left = (i ==0 ) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) -1) or (flowerbed[i + 1] == 0)
            if left and right and flowerbed[i] ==0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
    
# TC: O(len(flowerbed)) -> 0(n)