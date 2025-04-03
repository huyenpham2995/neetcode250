# Question
https://leetcode.com/problems/design-hashset/description/

# Thoughts
## My Hash Set
- To keep the search, add and remove operation to O(1), there has to be a way to jump straight to the element (if it's available).
- The range of the input is from 1 -> 10^5, we will make the biggest array as we can, which contains 10^5 +1 slots.
- Then for each number, to find a place to insert it, just go straight to the array[key] position. It will give the number a unique position.
- Every goes straight forward from then one, to find, add or remove element from the array
    - To remove, just reset the position to 0.
    - To see if it contains, go to the position and see if the key is there
    - To add, just set the array element at the position to the key

# BigO
## My Hash Set
- Time: O(1) for all 3 operations
- Space: O(10^5), or O(N)