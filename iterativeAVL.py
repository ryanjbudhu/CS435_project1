from getRandArray import getRandArray
class Node:
	def __init__(self, val, parent=None):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent
		self.height = 1
		
def insertIter(root, val):
	global count
	newroot = root
	if root is None:
		root = Node(val)
		return root
	else:
		#insert the node
		cur = root
		while cur != None:
			if cur.val < val:
				if cur.right == None:
					cur.right = Node(val, cur)
					break
				else:
					cur = cur.right
					count += 1

			else:
				if cur.left == None:
					cur.left = Node(val, cur)
					break
				else:
					cur = cur.left
					count += 1

		#balance the tree
		while cur != None:
			cur.height = 1 + max(getAVLHeight(cur.left), getAVLHeight(cur.right))
			balance = getBF(cur)
			
			#left-left
			if balance > 1 and val < cur.left.val:
				cur = rightRotate(cur)

			# right-right 
			elif balance < -1 and val > cur.right.val:
				cur = leftRotate(cur)
			
			# left-right 
			elif balance > 1 and val > cur.left.val:
				cur.left = leftRotate(cur.left)
				cur = rightRotate(cur)
				
			# right-left
			elif balance < -1 and val < cur.right.val:
				cur.right = rightRotate(cur.right)
				cur = leftRotate(cur)
			
			newroot = cur
			cur = cur.parent
		return newroot


def deleteIter():
	global count
	if root == None:
		return
	cur = root
	while cur != None:
		if value < cur.val:
			cur = cur.left
		elif value > cur.val:
			cur = cur.right
			count += 1
		else:
			if cur.left == None:
				tmp = cur.right
				cur = None
				continue
			elif cur.right == None:
				tmp = cur.right
				cur = None
				continue
			tmp = findMinIter(cur.right)
			cur.val = tmp.val
			cur = cur.right
			count += 1
	
	while cur != None:
		cur.height = 1 + max(getAVLHeight(cur.left), getAVLHeight(cur.right))
		balance = getBF(cur)
		
		#left-left
		if balance > 1 and val < cur.left.val:
			cur = rightRotate(cur)

		# right-right 
		elif balance < -1 and val > cur.right.val:
			cur = leftRotate(cur)
		
		# left-right 
		elif balance > 1 and val > cur.left.val:
			cur.left = leftRotate(cur.left)
			cur = rightRotate(cur)
			
		# right-left
		elif balance < -1 and val < cur.right.val:
			cur.right = rightRotate(cur.right)
			cur = leftRotate(cur)
		
		newroot = cur
		cur = cur.parent
	return newroot

def findMaxIter(root):
	cur = root
	while cur.right != None:
		cur = cur.right
	return cur

def findMinIter(root):
	cur = root
	while cur.left != None:
		cur = cur.left
	return cur

def findNextIter(node):
	global count
	if node.right != None:
		count += 1
		return findMinIter(node.right)
	prnt = node.parent
	while prnt != None:
		if node != prnt.right:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
def findPrevIter(node):
	global count
	if node.left != None:
		count += 1
		return findMaxIter(node.left)
	prnt = node.parent
	while prnt != None:
		if node != prnt.left:
			break
		node = prnt
		prnt = prnt.parent
	return prnt

def getAVLHeight(node):
	if node is None:
		return 0
	return node.height

def getBF(node):
	if node is None:
		return 0
	return getAVLHeight(node.left) - getAVLHeight(node.right)

def printout(root):
	if root == None:
		return
	printout(root.left)
	print(root.val,root.height,getBF(root))
	printout(root.right)

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
count = 0
def test():
	#Create and build tree
	arr = getRandArray(10,end=100)
	root = Node(arr[0])
	for i in arr[1:]:
		root = insertIter(root, i)
		
	#Test the functions
	print(arr)
	print('Root:',root.val)
	maxNode = findMaxIter(root)
	minNode = findMinIter(root)
	print('Max:',maxNode.val)
	print('Min:',minNode.val)
	print('Next:',findNextIter(minNode).val)
	print('Prev:',findPrevIter(maxNode).val)
	print()
	printout(root)
test()