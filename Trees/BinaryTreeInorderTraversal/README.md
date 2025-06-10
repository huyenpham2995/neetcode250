# Question
https://leetcode.com/problems/binary-tree-inorder-traversal/

# Thoughts
- Inorder traversal of a binary tree: left -> right -> root
- If the root is empty, just return the empty list
- Then keeps going to the left
- Add the value to the result array, then goes to the right.

# BigO
- Time: O(N)
- Space: O(N)