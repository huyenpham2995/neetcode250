# Question
https://leetcode.com/problems/remove-element/

# Thoughts
- We don't really need to actually remove the val out of the array. The question only ask to move all the elements that are equal to val to the end of the array and return the # of elements that are not val.
- To do this, we can have 2 pointers travel from the front and the back. 
    - The front pointer keeps moving up until it hits an element that = val. 
    - If element = val, swap the element to the element at the end pointer and move the end pointer down.
    - Keep doing so until the start pointer meets the end pointer, then return the position of the start pointer (i.e, the number of elements that are not val).
- Even if the question asks to return the array without elements = vale, we can just return a portion of the array that does not have val in it.

# BigO
- Time: O(N)
- Space: O(1) (in place)