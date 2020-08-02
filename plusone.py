class Solution:
    def plusOne(self,digits):
        index = len(digits)-1
        temp = 1
        while (index > -1):
            print(index)
            if index != 0:
                if temp == 1:
                    digits[index]+=1
                    if digits[index] == 10:
                        digits[index] = 0
                        temp = 1
                    else:
                        temp = 0
            if index == 0:
                if temp == 1:
                    digits[index]+=1
                    if digits[index] == 10:
                        digits[index] = 0
                        return [1] + digits
            index-=1
        return digits
        

print(Solution().plusOne([1,2,3]))