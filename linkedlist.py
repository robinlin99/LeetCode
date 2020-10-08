class Node():
	def __init__(self,value):
		self.data = value
		self.next = None
	def printll(self):
		temp = self
		while temp != None:
			print(temp.data)
			temp = temp.next


def reverse(head):
	# (None) -> A -> B -> C -> D -> None 
	#  None <- A <- | B | <- C <- D
	prev = head
	curr = head.next
	prev.next = None
	while curr != None:
		nextcurr = curr.next
		curr.next = prev
		prev = curr
		curr = nextcurr
	return prev

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

def remove(node):
	curr = node.next
	temp = node
	hashmap = {}
	hashmap[temp.data] = True
	while curr != None:
		data = curr.data
		if data not in hashmap:
			temp.next = curr
			curr = curr.next
			temp = temp.next
			hashmap[data] = True
		else:
			curr = curr.next
		if curr == None:
			temp.next = None
	return node



a = Node(3)
a.next = Node(6)
a.next.next = Node(10)
a.next.next.next = Node(15)
a.next.next.next.next = Node(16)
a.next.next.next.next.next = Node(18)
a.next.next.next.next.next.next = Node(19)
a.next.next.next.next.next.next.next = Node(21)
a.next.next.next.next.next.next.next.next = Node(25)