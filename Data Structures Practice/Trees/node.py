class Node:
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None
	def inorder(self,node,accum):
		if node == None:
			return
		self.inorder(node.left,accum)
		print(node.val)
		accum.append(node.val)
		self.inorder(node.right,accum)
	def preorder(self,node,accum):
		if node == None:
			return
		print(node.val)
		accum.append(node.val)
		self.preorder(node.left,accum)
		self.preorder(node.right,accum)
	def postorder(self,node,accum):
		if node == None:
			return
		self.postorder(node.left,accum)
		self.postorder(node.right,accum)
		print(node.val)
		accum.append(node.val)

root = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)
root.left = nodeB
root.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
print("Inorder")
a = []
b = []
c = []
root.inorder(root,a)
print("Preorder")
root.preorder(root,b)
print("Postorder")
root.postorder(root,c)
print(a)
print(b)
print(c)