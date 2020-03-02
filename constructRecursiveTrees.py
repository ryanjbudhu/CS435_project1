from getRandArray import getRandArray
#BST
from recursiveTree import printout, insertRec, Node#,findMinRec,findMaxRec
#AVL
from recursiveAVL import insertRec as insertRecAVL
from recursiveAVL import Node as NodeAVL
import time

arr = getRandArray(10000)

#BST
startBST = time.time()
rootBST = Node(arr[0], None)
for i in arr[1:]:
	insertRec(rootBST, Node(i))
endBST = time.time()
timeBST = round(endBST - startBST, 6)
print('BST:',timeBST)
#printout(rootBST)

#AVL
startAVL = time.time()
rootAVL = NodeAVL(arr[0])
for i in arr[1:]:
	insertRecAVL(rootAVL, i)
endAVL = time.time()
timeAVL = round(endAVL - startAVL, 6)
print('AVL:',timeAVL)