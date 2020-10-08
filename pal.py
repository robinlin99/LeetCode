class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            if int(str(x)[::-1]) == x:
                return True

        """
        :type x: int
        :rtype: bool
        """
