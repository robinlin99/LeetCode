class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        beginindex = -1
        curr = 0
        accum = ""
        needleindex = 0
        for i in haystack:
            if i == needle[needleindex]:
                if needleindex == 0:
                    beginindex=curr
                accum+=i
                needleindex+=1
            else:
                beginindex = -1
                accum = ""
                needleindex = 0 
            if accum == needle:
                return beginindex
            print(accum,i)
            curr+=1
        return -1
                
            
Solution().strStr("mississippi",
"issip")
        
            
        