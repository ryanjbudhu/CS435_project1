from getRandArray import getRandArray
class Node:
	def __init__(self, val, parent):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent
		
def insertRec(root, val):
	insertIterHelper(root, val)

def insertIterHelper(root, val):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right == None:
				root.right = node
				root.right.parent = root
			else:
				insertRec(root.right, node)
		else:
			if root.left == None:
				root.left = node
				root.left.parent = root
			else:
				insertRec(root.left, node)