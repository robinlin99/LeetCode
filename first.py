class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, j in enumerate(s):
            if j not in s[i+1:len(s)+1] and j not in seen:
                return i
            if j in seen:
                seen[j] +=1
            if s[i] not in seen:
                seen[j] = 1
        return -1
            
print(Solution().firstUniqChar('cc'))