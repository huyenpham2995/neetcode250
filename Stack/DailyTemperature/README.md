# Question
https://leetcode.com/problems/daily-temperatures/

# Thoughts
- This is the problem where we can utilize stack with the indicies of the elements to determine the number of day.
- We can keep an array of the same size with the input array, initilize with all 0
- Also keep a stack to keep track of the indicies. The rule is of following: if the temperature at the current index is less than the last index (i.e, the top of the stack), add the current index to the stack. If we hit a temperature that is larger than the previous one, pop the top of the stack to get the index, then the day will be the current index - that popped index.
- Go through all temps in the temperatures array:
    - If stack is empty or current temp is less than or equal to the temp at the index at the top of the stack, push the index into the stack
    - Else:
        - Pop the last index out of the stack.
        - Calculate the day by taking the current index - the popped index.
        - Keep popping until the temp at the current index is not greater than the temp of an index in the stack.
        - Add the current index to the stack.
        
# BigO
- Time: O(N)
- Space: O(N)