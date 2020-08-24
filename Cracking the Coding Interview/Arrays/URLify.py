def replace(string):
	accum = ""
	# O(N) solution
	for i, char in enumerate(string):
		if char != " ":
			accum += char
		if char == " " and string[i-1] != " ":
			accum += "%20"
	return accum

print(replace("Hello world     this is a test"))
