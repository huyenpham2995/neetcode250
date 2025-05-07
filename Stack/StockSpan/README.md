# Question
https://leetcode.com/problems/online-stock-span/description/

# Thoughts
- We need a non-increasing stack and another stack to keep track of the spanning day. The stack will contains tuples of (price, count).
- When a new value is added to the stack
    - Initialize count to 1
    - If the stack is empty, add the price and count to the stack
    - Else
        - While the top of the stack is less than or equal to the current price, pop that out of the stack. Add its count to the current count
        -  If we hit a price that is greater than current price, or we have kick everyone out of the stack, add the current price and count to the stack.

# BigO
- Time: O(N)
- Space: O(N)