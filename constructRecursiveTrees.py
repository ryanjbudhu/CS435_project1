from getRandArray import getRandArray
#BST
from recursiveTree import printout, insertRec, Node#,findMinRec,findMaxRec
#AVL
import time

arr = getRandArray(10000)

#BST
startBST = time.time()
rootBST = Node(arr[0], None)
for i in arr[1:]:
	insertRec(rootBST, Node(i))
endBST = time.time()
timeBST = round(endBST - startBST, 6)
print(timeBST)
#printout(rootBST)

#AVL
startAVL = time.time()
#[CODE]
endAVL = time.time()
timeAVL = round(endAVL - startAVL, 6)
print(timeAVL)