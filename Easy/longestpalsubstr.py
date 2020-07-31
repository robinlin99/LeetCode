class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxn = 0
        longest = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substr = s[i:j]
                if substr[::-1] == substr:
                    if len(substr) > maxn:
                        maxn = len(substr)
                        longest = substr
        return longest
                
        