class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # characters in balloon string
        list = {'b':0,'a':1,'l':2,'o':3,'n':4}
        count = [0,0,0,0,0]
        found = [0,0,0,0,0]
        for i in text:
            if i in list:
                # increment character counter by 1 every time found in                      dictionary
                count[list[i]] += 1
        for i in range(0,len(count)):
            if i == list['l'] or i == list['o']:
                found[i] = count[i]/2
            else:
                found[i] = count[i]
                
        # return minimum element in the list
        return min(found)
        
        
        
        
        
                