# Question
https://leetcode.com/problems/majority-element-ii/

# Thoughts
## Approach 1: dictionary and set
- Create a dictionary and keep count of the occurence of each number
- Keep a `res` set to record the elements
- Go through the array and add 1 to the occurence every time we encounter the number
    - If the number count exceeds n/3 and the number is not already in the `res` set, add the number to the set

# BigO
## Approach 1
- Time: O(N)
- Space: O(N)