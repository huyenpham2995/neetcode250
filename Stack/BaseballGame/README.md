# Question
https://leetcode.com/problems/baseball-game/

# Thoughts
- We can use stack to solve this problem. All new numbers got push into the top of the stack, the first ones to be processed are the ones fromt he top of the stack.
- Go through the whole array
    - If encounter "C", just pop the top one out of the stack
    - If encounter a "+", peek the top 2 of the stack, take a sum and add that sum to the top of the stack
    - If encounter a "D", peek the top of the stack, double that number and add that to the top of the stack.
    - The only thing left is a number itself, so just convert it from a string to an int and push it to the top of the stack.
- Take the sum of the whole stack then return it.

# BigO
- Time: O(N)
- Space: O(N)