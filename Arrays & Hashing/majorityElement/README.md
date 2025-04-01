# Question
https://leetcode.com/problems/majority-element/submissions/1588877387/

# Thoughts
## Approach 1: sort
- Sort the array in any order (descendent or ascendent).
- Keep track of the count of each number. If the count exceed n/2, return the number immediately.

## Approach 2: dictionary
- As we loop through the array, keep the count of each number by creating a dictionary with key = number, value = count
- Immediately return when count of any number > n/2

## Approach 3:  Boyer-Moore Algorithm
- This algorithm will work AND ONLY WORK when **there is a guarateed number that is the majority in the array**
- The idea: 
    - We keep count of the current result that we assume is the most appeared in the array. Every time we hit a number that is equal to the current res, increase the count.
    - If the number we hit is not res, there are 2 options:
        - Decrease the count if the count > 0
        - If the count is already 0, we will have to change our assumption about our result to be the new number.
- Why does this work? The assumption we have is that the majority number will have the most count out of the array. There is no other number that have the same count, or else the array has no majority number. So at the end, the number who can keep the most count will win.
- The way it works for [1,1,2,2,2,1,1]:
    - We keep only 2 elements: the res, which is the result, and the count.
    - At num = 1, set res = 1, count = 1
    - At num = 1, keep res = 1, count = 2,
    - Now num = 2. It is not 1 anymore, so keep res = 1, decrease count = 1
    - At num = 2, keep res = 1, decrease count = 0
    - At num = 2, since count is 0, we will switch res = 2, and the count of res = 1
    - At num = 1, it is not 2 anymore, so keep res = 2, decrease count = 0
    - At num = 1, count is 0, change res = 2, count = 1
    - Return 2.

# BigO
## Approach 1
- Time: sort O(nlogn)
- Space: O(1)

## Approach 2
- Time: O(N)
- Space: O(N)

## Approach 3
- Time: O(N)
- Space: O(1)