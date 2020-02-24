from getRandArray import getRandArray
MAXINT = 999999
class Node:
	def __init__(self, val, parent=None):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None

def insertRec(root, node):
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
def deleteRec(root, value):
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
	return root
def findNextRec(start, node):
	if node.right != None:
		return findMinRec(node.right)
	prnt = node.parent
	while prnt != None:
		if node != prnt.right:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
	
def findPrevRec(start, node):
	if node.left != None:
		return findMaxRec(node.left)
	prnt = node.parent
	while prnt != None:
		if node != prnt.left:
			break
		node = prnt
		prnt = prnt.parent
	return prnt
	
def findMinRec(root):
	if root==None:
		return Node(MAXINT)
	res = root
	newres = findMinRec(root.left)
	if newres.val < res.val:
		res = newres
	return res
def findMaxRec(root):
	if root==None:
		return Node(-MAXINT)
	res = root
	newres = findMaxRec(root.right)
	if newres.val > res.val:
		res = newres
	return res

#Used to pretty print the tree in preorder
def printout(root):
	if root == None:
		return
	printout(root.left)
	print(root.val)
	printout(root.right)

#Create and fill out the tree
arr = getRandArray(10)
root = Node(arr[0], None)
for i in arr[1:]:
	insertRec(root, Node(i))

#Print out results of each function
print(arr)
print('Root:',root.val)
maxNode = findMaxRec(root)
minNode = findMinRec(root)
print('Max:',maxNode.val)
print('Min:',minNode.val)
nextNode = findNextRec(minNode, minNode)
print('Next:',nextNode.val)
nextNode2 = findNextRec(nextNode, nextNode)
print('Next2:',nextNode2.val)
prevNode = findPrevRec(maxNode,maxNode)
print('Prev:',prevNode.val)
prevNode2 = findPrevRec(prevNode,prevNode)
print('Prev2:',prevNode2.val)
print()
printout(root)