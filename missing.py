class Solution(object):
    def missingNumber(self, nums):
      # create a sorted list from nums
      # 0,1,2,4,5 -> check difference between adjacent components, if ok -> return max + 1, else return break element + 1
      
      # 0,1,n
      # 1,2
      nums.sort()
      difference = 1
      for i in range(0,len(nums)-1):
        if nums[i+1] - nums[i] != difference:
            return nums[i] + 1
      if 0 not in nums:
        return 0
      else:
        return nums[len(nums)-1] + 1
          