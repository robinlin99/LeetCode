class Solution:
	def reverseBits(self, n):
		rBinary = bin(n)[2:len(bin(n))][::-1]
		rval = 0
		print(rBinary)
		for i in range(0,len(rBinary)):
			rval += int(rBinary[i])*(2**(len(rBinary)-i-1))
		print(rval)


print(bin(43261596))
Solution().reverseBits(43261596)