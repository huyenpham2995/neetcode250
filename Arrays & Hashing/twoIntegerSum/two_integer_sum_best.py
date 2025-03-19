from typing import List

def twoSumBest(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i in range(len(nums)):
        if num_dict.get(target - nums[i], None) != None and i != num_dict[target - nums[i]]:
            return [num_dict[target - nums[i]], i]
        num_dict[nums[i]] = i
    
    return []