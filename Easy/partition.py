def partition(s,k):
	# split into unique substrings of size k with k distinct characters
	accum = []
	hashmap = {}
	for i in range(0,len(s)-k+1):
		substr = s[i:i+k]
		if substr not in hashmap:
			hashmap[substr] = True
			hashmapchar = {}
			duplicate = False
			for i in substr:
				if i not in hashmapchar:
					hashmapchar[i] = True
				else:
					duplicate = True
			if duplicate == False:
				accum += [substr]

	return accum


s = "abacab"
k = 3
print(partition(s,k))
assert(partition(s,k) == ["bac", "cab"])


s = "abcabc"
k = 3
print(partition(s,k))
assert(partition(s,k) == ["abc", "bca", "cab"])