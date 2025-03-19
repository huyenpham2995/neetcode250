# Question
https://leetcode.com/problems/two-sum/ 

# Thoughts
## My initial approach
- The brute force is obvious: go through each number, then find the target - that number in the array, if yes return the index, no move on.
    - Pros: save space, only use 2 pointers
    - Cons: time O(N^2)
- My 2nd thought was to save some time:
    - Go through the list of nums one time, time store the num and their index in a dictionary (key: num, val: index).
    - Go through the nums list one more time. This time, for each num, find target-num in the dictionary. If that exists, return the indexes right away.
    - The problem with this method is duplicated number. For example: if the list is [3,3], then my dictionary only has {3: 1} (the index 0 got replaced). Then the return value is [1,1] instead of [0,1]. The rule is we cannot use a number twice.
    - After that, I change the dictionary value to a list. So key is still num, value is the list of indexes with the same num. Eg: {3: [0,1]}.
        - Every time an index is used, it's popped out of the value list, until nothing is left.

## A Better Way
- Very similar to my first solution, I will still keep a dictionary of {num: index}. It's okay to not keep all the indexes of a number, because the assumption (big assumption) is there is only 1 pair of solution.
- So in the case of [3,3], the dictionary is {3:1}. Then when I traverse the list for the 2nd time, the returning result will be [current index, dictionary index] instead of getting all the indexes from the dictionary like before. So when Im at index 0, I'll return 
`[current index=0, dictionary index=1]`. To prevent using a number 2 times, I just need to add a condition that the `current index != dictionary index`

## The Best Way
- The best way requires only going through the list one time and still utilize dictionary. For each time
    - See if target-current is in the dictionary and the indexes are different, if it is, return the result right away.
    - If not, add the current number to the dictionary.
- The only difference is that the result return will be the index of target-current first, then current, since it is going "backward" to check for target-current instead of going forward like the other 2 approaches.

# BigO
- Space: keep a dictionary of all numbers -> O(N)
- Time: either going through the list one or 2 times, the bigO will be O(N)