# Question
https://leetcode.com/problems/range-sum-query-2d-immutable/

# Thoughts
- The obvious solution was to go through each slot and calculate the sum. In the worst case scenario, the runtime is O(N^2).
- To make it better, we calculate the prefix sum at each slot when we initialize the 2D array. We create a separate array of size (N+1) x (N+1) (prefix sum array) to store these sum (will explain why it is N+1 later).
  
    ![Initialize](IMG_4764.heic)
  - Each slot will store the sum of the red region as shown in the picture, basically from the first slot expand to itself. How do we calculate this?
      - The prefix sum of the slot above the current slot (the pink region) has been calculated from the previous round.
      - For the current row of this slot, as we travel through this row, we can keep track of the sum from the beginning of the row to the current slot (the yellow region).
      - The prefix sum of the current slot is the sum of those 2, and can always be calculated in O(1) time.
      - Store the sum in the "equivalent" position in the prefix sum array.
  -  Now after finish calculating the prefix sum, we can calculate any region within this 2D array.
  
    ![region sum](IMG_4765.heic)
      - Basically, the bolded region will be calculated by taking the prefix sum of the bottom slot (the yellow region), minus the prefix sum of the red regions (prefix sum of (2,0) and prefix sum of (0,2) in this example) and add back prefix sum of (0,0) (because the 2 red regions overlapped there so it was deducted 2 times).
      - For the edge case of having to calculate the sum in the edge of the array, moving left or up from it will cause index out-of-range, that is why our prefix sum array will have 1 more row and one more column. The extra slots will be all 0 to compensate for these edge cases.
      - The region sum that we need will be: `prefix sum of (row2,col2) - prefix sum of (row2,col1-1) - prefix sum of (row1-1,col2) + prefix sum of (row1-1, col1-1)`, which will be calculated in O(1) time.

# BigO
- Space: (N+1) ^ 2 -> O(N^2)
- Time:
    - Create prefix matrix: O(N^2)
    - Get Region sum: O(1)
