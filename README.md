1. Binary Search Tree
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
  + c) [CODE]
  + d) [CODE]
	
2. Sort it!
    + 0005, 0006, 0007, 0010, 0011, 0012, 0016, 0017, 0018, 0019, 0020
    + Insert the values into the BST one at a time, then create an array of a breadth-first traversal of the BST and output the array.
    + [CODE✓]
	
3. Arrays of Integers
    + [CODE✓]
    + [CODE ✓]
