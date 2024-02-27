# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        while i < len(flowerbed):
            if (i==0 or flowerbed[i-1]==0)and (flowerbed[i]==0)and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n=n-1
                i=i+2
            else:
                i=i+1
        return n<=0

s = Solution()

print(s.canPlaceFlowers([1,0,0,0,1], 1))
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))
print(s.canPlaceFlowers([0,0,1,0,1], 1))
