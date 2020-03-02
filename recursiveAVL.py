from getRandArray import getRandArray

class Node:
	def __init__(self, val, parent=None):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1
		self.parent = parent

def insertRec(root,val):
	if root is None:
		return Node(val, root)
	elif root.val > val:
		root.left = insertRec(root.left, val)
	else:
		root.right = insertRec(root.right, val)
	
	root.height = 1 + max(getAVLHeight(root.left), getAVLHeight(root.right))
	balance = getBF(root)

	# lef-left
	if balance > 1 and val < root.left.val:
		return rightRotate(root)

	# right-right 
	if balance < -1 and val > root.right.val:
		return leftRotate(root)
	
	# left-right 
	if balance > 1 and val > root.left.val:
		root.left = leftRotate(root.left)
		return rightRotate(root)
		
	# right-left
	if balance < -1 and val < root.right.val:
		root.right = rightRotate(root.right)
		return leftRotate(root)
	
	return root

def deleteRec(root, val):
	if root == None:
		return root
	if value < root.val:
		root.left = deleteRec(root.left, value)
	elif value > root.val:
		root.right = deleteRec(root.right, value)
	else:
		if root.left == None:
			tmp = root.right
			root = None
			return tmp

		elif root.right == None:
			tmp = root.left
			root = None
			return tmp

		tmp = findMinRec(root.right)
		root.val = tmp.val
		root.right = deleteRec(root.right, tmp.val)
	
	root.height = 1 + max(getAVLHeight(root.left), getAVLHeight(root.right))
	balance = getBF(root)

	# lef-left
	if balance > 1 and val < root.left.val:
		return rightRotate(root)

	# right-right 
	if balance < -1 and val > root.right.val:
		return leftRotate(root)
	
	# left-right 
	if balance > 1 and val > root.left.val:
		root.left = leftRotate(root.left)
		return rightRotate(root)
		
	# right-left
	if balance < -1 and val < root.right.val:
		root.right = rightRotate(root.right)
		return leftRotate(root)
	
	return root

def isLeftChild(node):
	return node.parent and node.parent.left == node

def isRightChild(node):
	return node.parent and node.parent.right == node

def leftRotate(b):
	a = b.right
	b.right = a.left
	if a.left != None:
		a.left.parent = b
	a.parent = b.parent
	if b.parent is None:
		root = a
	else:
		if isLeftChild(b):
			b.parent.left = a
		else:
			b.parent.right = a
	a.left = b
	b.parent = a


	b.height = max(getAVLHeight(b.left), getAVLHeight(b.right)) + 1
	a.height = max(getAVLHeight(a.left), getAVLHeight(a.right)) + 1
	
	return a

def rightRotate(b):
	a = b.left
	b.left = a.right
	if a.right != None:
		a.right.parent = b
	a.parent = b.parent
	if b.parent is None:
		root = a
	else:
		if isRightChild(b):
			b.parent.right = a
		else:
			b.parent.left = a
	a.right = b
	b.parent = a
	
	b.height = max(getAVLHeight(b.left), getAVLHeight(b.right)) + 1
	a.height = max(getAVLHeight(a.left), getAVLHeight(a.right)) + 1
	
	return a

def getAVLHeight(root):
	if not root:
		return 0
	return root.height

def getBF(root):
	if not root:
		return 0
	return getAVLHeight(root.left) - getAVLHeight(root.right)

def findMinRec(root):
	if root is None or root.left is None:
		return root
	return findMinRec(root.left)
def findMaxRec(root):
	if root is None or root.right is None:
		return root
	return findMaxRec(root.right)
	
def findPrevRec(node):
	if node.left != None:
		return findMaxRec(node.left)
	prnt = node.parent
	while prnt != None:
		if node != prnt.left:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
	
def findNextRec(node):
	if node.right != None:
		return findMinRec(node.right)
	prnt = node.parent
	while prnt != None:
		if node != prnt.right:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
def printout(root):
	if root is None:
		return
	printout(root.left)
	print(root.val, root.height, getBF(root))
	printout(root.right)

def test():
	arr = getRandArray(10)
	print(arr)
	root = Node(arr[0])
	for i in arr[1:]:
		root = insertRec(root, i)

	printout(root)		
	minNode = findMinRec(root)
	maxNode = findMaxRec(root)
	print('Min:',minNode.val)
	print('Max:',maxNode.val)
	print('Next:',findNextRec(minNode).val)
	print('Prev:',findPrevRec(maxNode).val)
#test()