#345. Reverse Vowels of a String
#https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        vowelArr = []
        newStr = ''

        for ch in s:
            if ch in vowels:
                vowelArr.append(ch)

        for ch in s:
            if ch in vowels:
                newStr += vowelArr[-1]
                vowelArr.pop(-1)
            else:
                newStr += ch

        return newStr

s = Solution()       
# print(s.reverseVowels("hello"))
# print(s.reverseVowels("leetcode"))
print(s.reverseVowels("aA"))
