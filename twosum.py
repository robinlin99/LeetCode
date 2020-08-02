class Solution:
	def twoSum(self, numbers, target):
		for i in range(0,len(numbers)):
			if target - numbers[i] in numbers[i+1:len(numbers)]:
				print('Index1',i)
				print('sublist',numbers[i+1:len(numbers)])
				print(numbers[i+1:len(numbers)].index(target-numbers[i]))
				return [i+1,numbers[i+1:len(numbers)].index(target-numbers[i])+i+2]


print(Solution().twoSum([5,25,75],100))