class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        max = 0
        for i in range(0,l+1):
            for j in range(0,l+1):
                substr = s[i:j]
                lsubstr = len(substr)
                if lsubstr != 0:
                    if repeated(substr) == False:
                        if lsubstr > max:
                            max = lsubstr
        return max
                    
            
def repeated(s):
    hashmap = {}
    for i in range(0,len(s)):
        if s[i] in hashmap:
            return True
        else:
            hashmap[s[i]] = 1
    return False
    
                
        