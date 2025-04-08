from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    output = [1]*len(nums)

    prefix = 1
    for i in range (len(nums)):
        output[i] = prefix
        prefix = prefix * nums[i]
    postfix = 1
    for i in range (len(nums)-1,-1,-1):
        output[i] = output[i] * postfix
        postfix = postfix * nums[i]

    return output