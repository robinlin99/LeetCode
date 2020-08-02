def pair(list,target):
	#list = input list, target -> find pair that multiply to target
	processed = []
	quotient = 0
	# O(N) time complexity
	# [0,1,2,3,...,N-1,N] loop until N-1 index, create processed sublist from n+1 to N, where n is current index
	for i in range(0,len(list)-1):
		if target % list[i] == 0:
			processed = list[i+1:len(list)]
			quotient = target/list[i]
			if quotient in processed:
				return (list[i],quotient)
	return False

list = [1,2,3,7]
target = 21

rval = pair(list,target)
print(rval)