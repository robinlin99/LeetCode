class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allcap = True
        nocap = True
        firstcap = True
        index = 0
        for i in word:
            if allcap is True:
                if i.islower():
                    allcap = False
            if nocap is True:
                if i.isupper():
                    nocap = False
            if firstcap is True:
                if index == 0 and i.islower():
                    firstcap = False
                if index != 0 and i.isupper():
                    firstcap = False
            index+=1
        print(allcap or nocap or firstcap)
        return (allcap or nocap or firstcap)
            
        
sol = Solution()
sol.detectCapitalUse('dfSf')