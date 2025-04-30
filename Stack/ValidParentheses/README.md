# Question
https://leetcode.com/problems/valid-parentheses/

# Thoughts
- Have a matching dictionary to match the open parentheses with its closing one (key is the open parentheses, value is the equivalent closing one).
- Go through the string:
    - If the character is the open parenthese, add it on top of the stack.
    - Else:
        - If the stack is empty (meaning the string go straight to closing without the opening parentheses), this is an invalid parenthesis, return False
        - Else, pop out the top of the stack. If this one matches the closing parentheses, continue. If not, return False (invalid).
- By the end of the string, if the stack is still not empty, return False since it is missing closing parentheses.
- Else return True.

# BigO
- Time: O(N)
- Space: O(N) (the stack)