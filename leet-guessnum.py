#374. Guess Number Higher or Lower
#https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#
#this was done on the sites envioronment

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right  = n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid -1
            elif guess(mid) == 1:
                left= mid +1 