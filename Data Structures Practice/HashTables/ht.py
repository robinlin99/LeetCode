class HashTable:
	def __init__(self,n):
		self.ht = {}
		self.size = n
		for i in range(n):
			self.ht[i] = []
	def insert(self,x):
		hashkey = self.hashfunction(x)
		self.ht[hashkey].append(x)
	def hashfunction(self,x):
		summation = 0
		for i in x:
			summation += ord(i)
		return summation % self.size

with open('values.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
print(content)
ht = HashTable(1000)
for i in content:
	ht.insert(i)
for key in ht.ht:
	print(key,ht.ht[key])


	