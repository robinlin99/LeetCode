class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ''
        b = ''
        for i in range(0,len(s)):
            if s[i] not in a:
                a = a + s[i]
            else:
                if len(a) > len(b):
                    b = a
                a = a[a.index(s[i])+1:]+s[i]
            print(a,b)
        print(max(len(a),len(b)))
                
                
          
a = Solution()
a.lengthOfLongestSubstring("jbpnbwwd")
