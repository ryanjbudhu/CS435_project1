# Ryan Budhu
## Section 004
---
### 1. Binary Search Tree
  + a) Properties of a BST.
    * Each node has a maximum of two children
    * The left subtree (all of the nodes coming from and including the left child) must be smaller than the root node
    * The right subtree (all of the nodes coming from and including the right child) must be greater than the root node
  + b) Where n = number of nodes in the BST
    - i. Insert –	O(n)
      * Worst case is when BST is a linked-list
    - ii. Delete –	O(n)
      * Worst case is when BST is a linked-list
    - iii. Find-next –	O(1)
      * Constant time with pointers that are saved (node.left, node.right)
    - iv. Find-prev –	O(1)
      * Constant time with pointer that is saved (node.parent)
    - v. Find-min –	O(n)
      * Must traverse to left most node
    - vi. Find-max –	O(n)
      * Must traverse to right most node
  + c) [recursiveTree.py ✓]
    - i. Create functions of a Binary Search Tree that implement the algorithms recursively.
	- ii. Input is valid and are integers, and integers are from range -999999 to 999999. There are also no duplicate numbers.
	- iii. Test Cases
		* Input:
		``[2428, 3147, 3222, 30, 7195, 5620, 5934, 2976, 1245, 5021]``
		  * Output:
			```
			Root: 2428
			Max: 7195
			Min: 30
			Next: 1245 (Where input is minimum node)
			Prev: 5934 (Where input is maximum node)
			```
	- iv. 
	- v. I use a max/min integer to check the minimum and maximum of the tree. Input must be greater than/less than for algorithm to work.
	- vi. ``recusiveTree.py``
	- vii. Use a different way of comparing for max and min in the tree.
  + d) [iterativeTree.py ✓]
	- i. Create functions of a Binary Search Tree that implement the algorithms recursively.
	- ii. Input is valid and are integers, and integers are from range -999999 to 999999. There are also no duplicate numbers.
	- iii. Test Cases
		* Input:
		``[6668, 8170, 4097, 2130, 4539, 3772, 482, 8277, 8952, 8451]``
		  * Output:
			```
			Root: 6668
			Max: 8952
			Min: 482
			Next: 2130 (Where input is minimum node)
			Prev: 8451 (Where input is maximum node)
			```
	- iv. 
	- v. I use a max/min integer to check the minimum and maximum of the tree. Input must be greater than/less than for algorithm to work.
	- vi. ``IterativeTree.py``
	- vii. Use a different way of comparing for max and min in the tree.
	
### 2. Sort it!
    + 0005, 0006, 0007, 0010, 0011, 0012, 0016, 0017, 0018, 0019, 0020
    + Insert the values into the BST one at a time, then create an array of a breadth-first traversal of the BST and output the array.
    + [BST.py ✓]
	
### 3. Arrays of Integers
    + [getRandomArray.py ✓]
    + [getSortedArray.py ✓]
