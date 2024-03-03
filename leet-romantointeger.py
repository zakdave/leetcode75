#13. Roman to Integer - https://leetcode.com/problems/roman-to-integer/description/

class Solution():
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0

        while i < len(s):
            
            # I
            if s[i] == 'I':
                if i+1 < len(s) and s[i+1] != 'I':
                    if s[i+1] == 'V':
                        ans += 4
                        i+= 2
                        continue
                    if s[i+1] == 'X':
                        ans += 9
                        i+= 2
                        continue
                ans+= 1
                i+= 1
                continue

            # X
            if s[i] == 'X':
                if i+1 < len(s) and s[i+1] != 'X':
                    if s[i+1] == 'L':
                        ans += 40
                        i+= 2
                        continue
                    if s[i+1] == 'C':
                        ans += 90
                        i+=2
                        continue
                ans+= 10
                i+= 1
                continue

            # C
            if s[i] == 'C':
                if i+1 < len(s) and s[i+1] != 'C':
                    if s[i+1] == 'D':
                        ans += 400
                        i+= 2
                        continue
                    if s[i+1] == 'M':
                        ans += 900
                        i+=2
                        continue
                ans+= 100
                i+=1
                continue

            if s[i] == 'V':
                ans += 5
            if s[i] == 'L':
                ans += 50
            if s[i] == 'D':
                ans += 500
            if s[i] == 'M':
                ans += 1000
            i+=1

        return ans
    
s = Solution()
print(s.romanToInt('II'))
print(s.romanToInt('III'))
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('V'))
print(s.romanToInt('VI'))
print(s.romanToInt('XVII'))
print(s.romanToInt('XIV'))
print(s.romanToInt('XIII'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))