def permupal(string):
	hashmap = {}
	# O(N) solution
	for char in string:
		if char not in hashmap:
			hashmap[char] = 1
		else:
			hashmap[char] += 1
	odd = []
	for char in hashmap:
		if hashmap[char] % 2 != 0:
			odd.append(char)
	print(odd)
	return len(odd) == 0 or len(odd) == 1

print(permupal("aabbCc"))
