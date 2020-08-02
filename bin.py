class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        inta = 0
        intb = 0
        for i in range(la-1,-1,-1):
            inta += int(a[i])*2**(la-i-1)
        for i in range(lb-1,-1,-1):
            intb += int(b[i])*2**(lb-i-1)
        print(inta,intb)
        return bin(inta+intb).replace('0b','')

print(Solution().addBinary('1010','1011'))
