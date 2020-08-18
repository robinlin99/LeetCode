class Solution:
    def reverse(self, x: int) -> int:
        # return 0 if reversed int is greater than 2**31 - 1 or less than -2**31
        strX = str(x)
        revstrX = strX[::-1]
        # strip zeros
        if revstrX[0] == '0':
            endIndex = 0
            while revstrX[endIndex] == '0':
                endIndex +=1
            revstrX = revstrX[endIndex:]
        if revstrX[-1] == '-':
            revstrX = revstrX[:-1]
            revstrX = '-' + revstrX
        return revstrX
                


integer = 1102000
print(Solution().reverse(integer))         
        
        
        
        