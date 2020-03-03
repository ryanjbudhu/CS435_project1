from getRandArray import getRandArray
class Node:
	def __init__(self, val, parent):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent

def insertIter(root, val):
	global count
	if root is None:
		root = Node(val)
		return
	else:
		cur = root
		while cur != None:
			if cur.val < val:
				if cur.right == None:
					cur.right = Node(val, cur)
					count += 1
					return
				else:
					cur = cur.right
					count += 1
			else:
				if cur.left == None:
					cur.left = Node(val, cur)
					count += 1
					return
				else:
					cur = cur.left
					count += 1
def deleteIter(root, value):
	global count
	if root == None:
		return
	cur = root
	while cur != None:
		if value < cur.val:
			cur = cur.left
			count += 1
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
	
def findMinIter(root):
	global count
	cur = root
	while cur != None:
		if cur.left == None:
			break
		cur = cur.left
		count += 1
	return cur
def findMaxIter(root):
	global count
	cur = root
	while cur != None:
		if cur.right == None:
			break
		cur = cur.right
		count += 1
	return cur

#To pretty print the tree
def printout(root):
	if root == None:
		return
	printout(root.left)
	print(root.val)
	printout(root.right)


count = 0
def test():
	global count
	#Create and build tree
	arr = getRandArray(10000)
	root = Node(arr[0], None)
	for i in arr[1:]:
		insertIter(root, i)
	#Test the functions
	#print(arr)
	print('Root:',root.val)
	maxNode = findMaxIter(root)
	minNode = findMinIter(root)
	print('Max:',maxNode.val)
	print('Min:',minNode.val)
	print('Next:',findNextIter(minNode).val)
	print('Prev:',findPrevIter(maxNode).val)
	print()
#	printout(root)
	print('count:',count)
#test()