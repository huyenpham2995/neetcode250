from collections import defaultdict
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    if len(set(nums)) <= k:
        return list(set(nums))
    
    bucket = [[] for i in range(len(nums))]
    res = []
    count = defaultdict(int)

    for num in nums:
        count[num] += 1
    for num,count in count.items():
        bucket[count-1].append(num)
    for i in range(len(bucket)-1,-1,-1):
        res = res + bucket[i]
        if len(res) == k:
            return res