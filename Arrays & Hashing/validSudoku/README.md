# Question
https://leetcode.com/problems/valid-sudoku/

# Thoughts
- The point of this question is literally just checking for any duplicates in any row, any column or any square, not to solve the sudoku.
- The brute force solution would be to check every rows, then check every columns, then check every squares, which means passing through the board at least 3 times.
- Optimal solution is to build a dictionary of the key being the index, the value being the set, and check to see if there's any duplicates
    - We need 3 dictionaries: for row, for column and for square
    - Go through each spot of the board
        - If it is empty (i,e "."), pass, not processing
        - If it is a number:
            - Add that number to the row dictionary (with key being the row of the number)
            - Add that number to the col dictionary (with key being the col of the number)
            - Add that number to the square dictionary (with key being (row //3, col//3))
                - Why // 3? The square is 3x3. So to belong in one square, the (r,c) of the mini square has to have the same value after // 3. For example, for the top left square, all (x,y) after // 3 will be (0,0). For the square to the right of it, it will be (1,0) and so on.
        - If the number is already in any of the set, immediately return false, since that's a duplicate.
    - If we can run through all the board without an issue, then return True.

# BigO
The board is of size NxN
- Time: O(N^2)
- Space: O(3N) -> O(N)