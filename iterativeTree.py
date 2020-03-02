from getRandArray import getRandArray
class Node:
	def __init__(self, val, parent):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent

def insertIter(root, val):
	if root is None:
		root = Node(val)
		return
	else:
		cur = root
		while cur != None:
			if cur.val < val:
				if cur.right == None:
					cur.right = Node(val, cur)
					return
				else:
					cur = cur.right
			else:
				if cur.left == None:
					cur.left = Node(val, cur)
					return
				else:
					cur = cur.left
def deleteIter(root, value):
	if root == None:
		return
	cur = root
	while cur != None:
		if value < cur.val:
			cur = cur.left
		elif value > cur.val:
			cur = cur.right
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
	
def findNextIter(node):
	if node.right != None:
		return findMinIter(node.right)
	prnt = node.parent
	while prnt != None:
		if node != prnt.right:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
def findPrevIter(node):
	if node.left != None:
		return findMaxIter(node.left)
	prnt = node.parent
	while prnt != None:
		if node != prnt.left:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
	
def findMinIter(root):
	cur = root
	while cur != None:
		if cur.left == None:
			break
		cur = cur.left
	return cur
def findMaxIter(root):
	cur = root
	while cur != None:
		if cur.right == None:
			break
		cur = cur.right
	return cur

#To pretty print the tree
def printout(root):
	if root == None:
		return
	printout(root.left)
	print(root.val)
	printout(root.right)



def test():
	#Create and build tree
	arr = getRandArray(10)
	root = Node(arr[0], None)
	for i in arr[1:]:
		insertIter(root, i)
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
#test()