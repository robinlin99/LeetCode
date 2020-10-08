class Node():
	def __init__(self,value):
		self.data = value
		self.next = None
	def printll(self,head):
		temp = head
		while temp != None:
			print(temp.data)
			temp = temp.next


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

n = Node(1)
n.next = Node(2)
n.next.next = Node(3)
n.next.next.next = Node(3)
n.next.next.next.next = Node(3)
n.next.next.next.next.next = Node(3)
n.printll(n)
print('-----')
h = remove(n)
h.printll(h)


