# Question
https://leetcode.com/problems/merge-strings-alternately/description/

# Thoughts
- If either of the strings are empty, return the other string.
- Run a loop to add the character alternatively until one of the string is done.
- If the strings have unequal length, after the llop, just add the rest characters of the longer string to the result.

# BigO
- Time: O(M+N)
- Space: O(1)