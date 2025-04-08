# Question
https://leetcode.com/problems/product-of-array-except-self/

# Thoughts
- This is a simple problem if we can use divide, since we can just calculate the product of all elements then loop through it again to divide the product with the current element to find the result.
- The constrain of not using divide makes us lean on addition of 2 sums: for each element, the product of all elements except itself is the product of all elements before it and all elements after it.
- First round: calculate the product of all elements before it
    - For the first element, there's nothing before it, so the product is 1
    - For any other element, the output is the product of the element right before it and the product of everything else before those 2 elemets. Those "everything else" can be pre-calculated and cached.
    - Eg [1,2,3,4]:
        - At first, the output is [1,1,1,1]. Keep a prefix (pre-calculated product)
        - At i=0, since there's nothing before it, the prefix = 1. Output is [1,1,1,1]
        - At i=1, the prefix = nums[0] * prefix = 1*1 = 1. Output is [1,1,1,1]
        - At i=2, the prefix = nums[1] * prefix = 2*1 = 2. Output is [1,1,2,1]
        - At i=3, the prefix = nums[2] * prefix = 3*2 = 6. Output is [1,1,2,6]
- Second round: calculate the product of all elements after it
    - Same theory as the first round but this time we are going backwards
    - Similarly, keep a postfix which is the product of everything after the current elements.
    - For the last element, there's nothing after it, so the postfix is 1
    - Eg [1,2,3,4]:  [24,12,4,1]
        - Again, the output is [1,1,1,1]. Postfix = 1
        - At i=3, since there's nothing before it, the postfix = 1. Output is [1,1,1,1]
        - At i=2, the postfix = nums[3] * postfix = 4*1 = 4. Output is [1,1,4,1]
        - At i=1, the postfix = nums[2] * postfix = 3*4 = 12. Output is [1,12,4,1]
        - At i=0, the postfix = nums[1] * postfix = 2*12 = 24. Output is [24,12,4,1]
- The final result will be the product at each position of these 2 output arrays: [1,1,2,6] and [24,12,4,1] -> [24,12,8,6]
- To save space, instead of creating another output array, we can just use the output array from the first round. So output[i] = output[i] * postfix

# BigO
- Time: O(2N) -> O(N)
- Space: O(1)
