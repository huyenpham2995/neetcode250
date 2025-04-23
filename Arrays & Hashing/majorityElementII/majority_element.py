from typing import List
from collections import defaultdict


def majorityElement2(nums: List[int]) -> List[int]:
    d = defaultdict(int)
    res = set()

    for num in nums:
        d[num] += 1
        if d[num] > len(nums)/3 and num not in res:
            res.add(num)
    
    return list(res)