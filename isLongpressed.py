class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # typed must have at least the input name string, plus repeated characters
        copy = []
        for i in name:
            copy.append(i)
        for j in range(0,len(typed)):
            if len(copy) != 0:
                if typed[j] == copy[0]:
                    copy = copy[1:len(copy)]
                else:
                    if typed[j] != typed[j-1]:
                        return False
            else:
                if typed[j] != typed[j-1]:
                        return False
        if len(copy) != 0:
            return False
                
        return True

                
            
            
            
            
            
        