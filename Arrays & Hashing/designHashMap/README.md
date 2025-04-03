# Question
https://leetcode.com/problems/design-hashmap/

# Thoughts
- This is exactly the same as hash set, but instead of having a boolean array, just have an array of values of the key.
- They key will be the index, the actual element is the value
- To indicate the key is not in the array, the initial array is filled with -1
- Since there are 10^6 elements, create an array of 10^6 + 1 slots.

# BigO
- Time: O(1)
- Space: O(10^6 + 1)