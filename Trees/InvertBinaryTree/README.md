# Question
https://leetcode.com/problems/invert-binary-tree/submissions/1674277817/

# Thoughts
- Binary tree: each node has exactly 2 children or no children at all (no unbalance level).
- DFS: Inorder traversal (handle the swap at the root, then go to the left, then the right).
- Steps:
    - Check to see if the root is empty, if it is return.
    - Swap the nodes from left to right, right to left.
    - Recursively moving to the left and repeat.
    - Recursively moving to the right and repeat.

# BigO
- Time: O(N)
- Space: O(N)