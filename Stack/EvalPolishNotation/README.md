# Question
https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Thoughts
- Whenever there's an opeartors, pop 2 top numbers out of the stack and perform the operator action. 
- Push back the result into the stack
- If it's a number just add it on top of the stack.

# BigO
- Time: O(N)
- Space: O(N)