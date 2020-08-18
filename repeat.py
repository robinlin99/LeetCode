def repeated(s):	
	s_length = len(s)
	hashmap = {}
	for i in s:
		if i in hashmap:
			return i
		else:
			hashmap[i] = 1
	return None
# assert(repeated('ABCA') == 'A'), 
print(repeated('ABCA'))
# assert(repeated('BCABA') == 'B'), 
print(repeated('BCABA'))
# assert(repeated('ABC') == None), 
print(repeated('ABC'))
