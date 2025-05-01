# Question
https://leetcode.com/problems/min-stack/

# Thoughts
- The naive solution is to find the min every time the function getMin() is called. But this will make getMin run in O(N) time.
- To make it O(1), we need to know the minimum number at every single level of the stack
- Eg: [-2,0,5,4,-3,6]
    - At -2, the min is -2
    - At 0, the min is -2
    - At 5, the min is -2
    - At 4, the min is -2
    - At -3, the min is -3
    - At 6, the min is -3
- So apart from the main stack, we have another stack called the min stack. In the previous example, the min stack will be [-2,-2,-2,-2,-3,-3]
- Every time an element is pop out of the stack, the equivalen is also pop out of the min stack. The min will have to be updated if necessary.
- When pushing to the stack:
    - Push to the main stack
    - If the new value is smaller than the current min, update the current min
    - Add that min to the min stack
- When popping out of the stack
    - Pop the main stack
    - Pop the min stack
    - Reset the min value my getting the top of the min stack.


# BigO
- Time: O(1) for all operations
- Space: O(N)