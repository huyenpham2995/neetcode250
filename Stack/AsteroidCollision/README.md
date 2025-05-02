# Question
https://leetcode.com/problems/asteroid-collision/

# Thoughts
- This is a tricky question due to some constraint and wording
    - The 2 asteroids collide when they are travelling in the opposite direction, the bigger one win. So basically if they are different "sign" (i.e their product is < 0, they will collide). HOWEVER, that is not entirely true. This only happens when the one on the left is traveling to the right, the one on the right is traveling to the left (i.e: right < left)
    - Eg: [-1, -2, 2, 1]
        - At first I thought -2 and 2 would collide, then 1 and -1 would collide.
        - But -1 and -2 are traveling to the left, while 2 and 1 are to the right, so they will never meet.
- With that, the condition are
    - The 2 asteroids have the product < 0
    - The left one > the right one
- Go through all asteroids:
    - At each asteroid, decide if we will add it to the stack
    - If the product of the 2 asteroids < 0 and right one <= left one
        - If the absolute of right > absolute of left, then the left one will be destroyed. We pop it out of the stack
        - Continue to compare the current asteroid with the next one in the stack until the weights are equal or the current asteroid is less weight. 
        - If the absolute of right < absolute of left, we don't add the right one in the stack
        - If the absolute of right == absolute of left, we don't add the right one and pop the left one out of the stack because both asteroids are destroyed.
    - In the case that the asteroids are traveling at the same direction, we add the current one into the stack.
    
# BigO
- Time: O(N)
- Space: O(N)