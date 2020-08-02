class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        copy = str(num)
        while len(copy) > 1:
            sum = 0 
            for j in copy:
                sum += int(j)
            copy = str(sum)
            
        return int(copy)
        