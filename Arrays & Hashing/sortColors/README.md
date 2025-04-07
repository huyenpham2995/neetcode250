# Question
https://leetcode.com/problems/sort-colors/description/

# Thoughts
## Approach 1: Count
- Count the number of each appearance of 0, 1 and 2. Then reconstruct the array using these appearance count.
- Eg: [1,1,0,2] - zero = 1 (time), one = 2 (times), two = 1 (time). Reconstruct array with one 0, two 1, one 2 -> [0,1,1,2]
- Go through the array one time to keep count, then go through it once again to modify the elements.

## Approach 2: three pointers
- One pointer called `s_pointer` to keep track of the smallest number, `l_pointer` to keep track of the large number. A `cur` pointer to traverse the list.
- The idea is `s_pointer` keep track of the position of the smallest element in the array, `l_pointe`r keep track of the largest. Therefore `s_pointer` starts from the beginning with cur, `l_pointer` starts from the end.
    - s_pointer = cur = 0
    - l_pointer = len(nums) - 1 (the end)
    - For sure we know, every elements **before** `s_pointer` position is 0, every elements **after** `l_pointer` is 2
- `cur` traverse through the arrar until `cur` meets `l_pointer` (everything after `l_pointer` is 2, no point to go further)
    - If nums[cur] is 0, swap element at `cur` and `s_pointer` (push 0 to the front), then increment `s_pointer` by 1. `cur` +1
    - If nums[cur] is 1, do nothing, just increment `cur`
    - If nums[cur] is 2, swap element at `cur` and `l_pointer` (push 2 to the back), then decrement `l_pointer`. Since we will only traverse until we meet `l_pointer`, the `cur` position is something that we are supposed to process when we go pass `l_pointer`, so we will not increment `cur`. We need to process that number now.
- Eg: [1,2,0]
    - [1,2,0], cur = s_pointer = 0, l_pointer = 2
        - nums[cur] = 2, do nothing
    - [1,2,0], cur = 1, s_pointer = 0, l_pointer = 2
        - nums[cur] = 2, swap, l_pointer = 1, keep cur
    - [1,0,2], cur = 1, s_pointer = 0, l_pointer = 1
        - nums[cur] = 0, swap, s_pointer = 1
    - [0,1,2], cur = 2, s_pointer = 1, l_pointer = 1
        - Now cur > l_pointer. Stop.
    

# BigO
## Approach 1
- Time: O(2N) -> O(N)
- Space: O(1) (keep 3 variables for the count).

## Approach 2
- Time: O(N)
- Space: O(1) (keep 2 pointers).
