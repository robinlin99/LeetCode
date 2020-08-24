def genpermutation(arr):
	accum = []
	length = len(arr)
	for i in range(2**length):
		bitstring = genbin(i,length)
		temp = []
		for bit, j in zip(bitstring, arr):
			if bit == "1":
				temp.append(j)
		accum.append([temp,bitstring])
	for i in accum:
		print(i)
	return accum

def genbin(n,maxlen):
	bitstring = bin(n)
	bitstring = bitstring[2:]
	if len(bitstring) < maxlen:
		bitstring = '0'*(maxlen-len(bitstring)) + bitstring
	return bitstring

print(genpermutation([1,2,3,4]))