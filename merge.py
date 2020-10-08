class Node():
	def __init__(self,value):
		self.data = value
		self.next = None
	def printll(self):
		temp = self
		while temp != None:
			print(temp.data)
			temp = temp.next


def merge(a,b):
	temp = Node(-1)
	head = temp
	atemp = a
	btemp = b
	while (atemp != None and btemp != None):
		if atemp.data <= btemp.data:
			temp.next = atemp
			atemp = atemp.next
		elif atemp.data > btemp.data:
			temp.next = btemp
			btemp = btemp.next
		temp = temp.next
	if atemp == None:
		temp.next = btemp
	if btemp == None:
		temp.next = atemp
	return head.next

a = Node(3)
b = Node(4)
a.next = Node(6)
b.next = Node(5)
a.next.next = Node(10)
b.next.next = Node(8)
a.next.next.next = Node(15)
b.next.next.next = Node(14)

# a.printll()
# b.printll()

c = merge(a,b)
c.printll()



