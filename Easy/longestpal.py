class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # there can only be 1 odd element
        # ex: aabaa -> one b, 4 a
        # empty dict
        odd = []
        even = []
        odd_max = 0
        accum = 0
        dict = {}
        for i in s:
          if i not in dict:
            dict[i] = 1
          else:
            dict[i] += 1
        for i in dict:
          if dict[i]%2 == 0:
            even.append(dict[i])
          else:
            odd.append(dict[i])
        if len(odd) != 0:
          odd_max = max(odd)
        accum = odd_max
        for j in even:
          accum += j
          
        return accum
          
            
        
            
        