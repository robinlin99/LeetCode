def partitionnonunique(s,k):
	# split into unique substrings of size k with k distinct characters
	accum = []
	for i in range(0,len(s)):
		for j in range(i+1,len(s)+1):
			substr = s[i:j]
			hashmapchar = {}
			counter = 0
			for char in substr:	
				if char not in hashmapchar:
					hashmapchar[char] = True
					# seen a new character
					counter = counter + 1
			if counter == k:
				accum += [substr]
	return len(accum)

s = "pqpqs"
k = 2
print(partitionnonunique(s,k))
assert(partitionnonunique(s,k) == 7)


s = "aabab"
k = 3
print(partitionnonunique(s,k))
assert(partitionnonunique(s,k) == 0)