from typing import List

def twoSum2(nums: List[int], target: int) -> List[int]:
    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i
    
    for i in range(len(nums)):
        if num_dict.get(target - nums[i], None) and i != num_dict[target - nums[i]]:
            return [i,num_dict[target - nums[i]]]
    return []  