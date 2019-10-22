class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        reverse = s[::-1]
        if len(s) == 1:
            return x
        if (s[0]=='-' and s[len(s)-1]=='0'):
            reverse = '-'+reverse[1:len(reverse)-1]

        elif (s[len(s)-1]=='0'):
            reverse = reverse[1:len(reverse)+1]

        elif (s[0]=='-'):
            reverse = '-'+reverse[0:len(reverse)-1]
        reverse_int = int(reverse)
        
        if reverse_int < -1*2**31 or reverse_int > 2**31-1:
            reverse_int = 0
        return reverse_int

        