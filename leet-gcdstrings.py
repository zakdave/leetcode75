# 1071. Greatest Common Divisor of Strings 
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # since str2 must be a prefix, we can weed out non-substrings
        if str1 + str2 != str2 + str1:
            return ''
        print(math.gcd(len(str2), len(str1)))
        return str1[:math.gcd(len(str2), len(str1))]
    
s = Solution()
print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("ABABAB", "AB"))
print(s.gcdOfStrings("LEET", "CODE"))