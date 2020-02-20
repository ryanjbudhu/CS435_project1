from getRandArray import getRandArray
MAXINT = 999999
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def insertRec(root, node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right == None:
				root.right = node
			else:
				insertRec(root.right, node)
		else:
			if root.left == None:
				root.left = node
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
def findNextRec(node):
	pass
def findPrevRec(node):
	pass
def findMinRec(root):
	if root==None:
		return MAXINT
	res = root.val
	newres = findMinRec(root.left)
	if newres < res:
		res = newres
	return res
def findMaxRec(root):
	if root==None:
		return -MAXINT
	res = root.val
	newres = findMaxRec(root.right)
	if newres > res:
		res = newres
	return res

def printout(root):
	if root == None:
		return
	printout(root.left)
	print(root.val)
	printout(root.right)


arr = getRandArray(10)
root = Node(arr[0])
for i in arr[1:]:
	insertRec(root, Node(i))

printout(root)
print('Max:',findMaxRec(root))
print('Min:',findMinRec(root))
deleteRec(root, findMinRec(root))

print()
printout(root)