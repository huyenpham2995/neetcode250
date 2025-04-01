from typing import List
from collections import defaultdict

def majorityElement1(nums: List[int]) -> int:
    cur = nums[0]
    count = 0

    for num in sorted(nums):
        if num == cur:
            count +=1
            if count > len(nums)/2:
                return num
        else:
            cur = num
            count = 1

def majorityElement2(nums: List[int]) -> int:
    num_dict = defaultdict(int)

    for num in nums:
        num_dict[num] += 1
        if num_dict[num] > len(nums)/2:
            return num
        
def majorityElementBest(nums: List[int]) -> int:
    res = 0
    count = 0

    for num in nums:
        if num != res:
            if count == 0:
                res = num
                count += 1
            else:
                count -= 1
        else:
            count += 1
    return res