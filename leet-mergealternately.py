#1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        solution = ""
        if len(word1) > len(word2):
            longest = len(word1)
        else:
            longest = len(word2)
        for i in range(longest):
            if i < len(word1):
                solution+= word1[i]
            if i < len(word2):
                solution+= word2[i]
        return solution

    
s = Solution()

print(s.mergeAlternately("abc","pqr"))
print(s.mergeAlternately("ab","pqrs"))

