def gen(s):
	s_len = len(s)
	for i in range(0,s_len):
		for j in range(i+1,s_len+1):
			print(s[i:j])


gen('abcd')