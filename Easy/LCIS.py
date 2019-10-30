class Solution(object):
    def findLengthOfLCIS(self, nums):
        max = 1
        accum = 1
        left = 0
        right = 1
        while right < len(nums):
          if nums[right] < nums[left]:
            accum = 0
          if nums[right] > nums[left]:
            accum+=1
          if accum > max:
            max = accum
          right+=1
          left+=1
        return max

x = Solution()
print(x.findLengthOfLCIS([1,2,3,4]))
print(x.findLengthOfLCIS([1,2,3]))
print(x.findLengthOfLCIS([1,2,4,3]))
print(x.findLengthOfLCIS([4,3,2,1]))
          
          
            
            
        