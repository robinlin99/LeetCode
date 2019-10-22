class Solution(object):
    def singleNumber(self, nums):
      dict = {}
      for i in nums:
        if i not in dict:
          dict[i] = 1
        else:
          dict[i] += 1
      for i in dict:
        if dict[i] == 1:
          return i
        