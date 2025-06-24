# Question
https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Thoughts
- The maximum depth of a tree is the depth of the left branch or the right branch, whichever is longer.
- If the root is empty, the depth is 0 (or if we are at leaf)
- Can calculate the depth of the whole tree by calculating the max depth of the subtree.
- Steps:
    - If root is empty, depth is 0.
    - Find the max depth of the substree
        - If the left branch is not empty, find the max depth of the left branch
        - If the right branch is not empty, find its depth.
        - Max depth is the longest one between the 2 that share a root.
        - +1 to that max depth (the root).

# BigO
- Time: O(N)
- Space: O(N)
