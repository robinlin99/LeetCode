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


a = Node(3)
a.next = Node(6)
a.next.next = Node(10)
a.next.next.next = Node(15)
a.next.next.next.next = Node(16)
a.next.next.next.next.next = Node(18)
a.next.next.next.next.next.next = Node(19)
a.next.next.next.next.next.next.next = Node(21)
a.next.next.next.next.next.next.next.next = Node(25)


c = reverse(a)
c.printll()



