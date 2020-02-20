from getRandArray import getRandArray
class Node:
	def __init__(self, val, parent):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent

def insertIter(root, val):
	pass
def deleteIter(root, value):
	pass
	
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

def printout(root):
	if root == None:
		return
	printout(root.left)
	print(root.val)
	printout(root.right)

arr = getRandArray(10)
root = Node(arr[0], None)
for i in arr[1:]:
	insertIter(root, i)

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
