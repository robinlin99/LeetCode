class Solution():
	def rot_compute(self,degrees,direction):
		assert degrees % 90 == 0
		assert direction in ["cw","ccw"]
		if degrees == 0:
			return 0
		else:
			if direction == "cw":
				return degrees/90
			else:
				return 4 - degrees/90
	def rotate(self,matrix,degrees,direction):
		copy = matrix.copy()
		n = int(self.rot_compute(degrees,direction))
		for i in range(0,n):
			temp = list(zip(*copy[::-1]))
			copy = [list(i) for i in temp]
		return copy

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
out = Solution().rotate(matrix,180,'ccw')
print("Before: ")
for i in matrix:
	print(i)
print("After Rotation: ")
for i in out:
	print(i)
