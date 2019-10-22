class Solution(object):
    def romanToInt(self, s):
        sum = 0
        for i in range(0,len(s)):
            if i < len(s) - 1:
                if  s[i] == 'I' and (s[i+1] == "V" or s[i+1] == "X"):
                    sum += -1*self.val(s[i])
                elif s[i] == 'X' and (s[i+1] == "L" or s[i+1] == "C"):
                    sum += -1*self.val(s[i])
                elif  s[i] == 'C' and (s[i+1] == "D" or s[i+1] == "M"):
                    sum += -1*self.val(s[i])
                else:
                    sum += self.val(s[i])
            if i == len(s) - 1:
                sum += self.val(s[i])
        return sum
            
            
    def val(self,str):
        if str == "I":
            return 1
        elif str == "V":
            return 5
        elif str == "X":
            return 10
        elif str == "L":
            return 50
        elif str == "C":
            return 100 
        elif str == "D":
            return 500   
        elif str == "M":
            return 1000

        
        