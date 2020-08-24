class BstNode:
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None
	def insert(self,node,root):
		if root == None:
			root = node
		if node.val > root.val:
			if root.right == None:
				root.right = node
			else:
				self.insert(node,root.right)
		if node.val < root.val:
			if root.left == None:
				root.left = node
			else:
				self.insert(node,root.left)
	def search(self,root,value):
		if root == None:
			return False
		if root.val == value:
			return True
		if root.val < value:
			return self.search(root.right,value)
		if root.val > value:
			return self.search(root.left,value)

root = BstNode(5)
node1 = BstNode(4)
node2 = BstNode(6)
root.insert(node1,root)
root.insert(node2,root)
print(root.search(root,5))
print(root.search(root,4))
print(root.search(root,6))
print(root.search(root,100))


