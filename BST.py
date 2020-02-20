class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value
def insert(root,node):
	if root is None: 
		root = node 
	else: 
		if root.val < node.val: 
			if root.right == None: 
				root.right = node 
			else: 
				insert(root.right, node) 
		else: 
			if root.left == None: 
				root.left = node 
			else: 
				insert(root.left, node)
def inorder(root, arr):
	if root:
		inorder(root.left, arr)
		arr.append(root.val)
		inorder(root.right, arr)

def sort(arr):
	root = Node(arr[0])
	for i in arr[1:]:
		insert(root, Node(i))
	ordered = []
	inorder(root,ordered)
	print(ordered)

tosort = [3,2,7,5,9]
sort(tosort)
