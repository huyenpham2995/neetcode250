from typing import List

def twoSum1(nums: List[int], target: int) -> List[int]:
    num_dict = {}

    for i in range(len(nums)):
        if not num_dict.get(nums[i], None):
            num_dict[nums[i]] = []
        num_dict[nums[i]] += [i]
    
    for num in nums:
        first_index = num_dict[num].pop(0)
        if num_dict.get(target - num, None):
            if num_dict[target - num] != []:
                return [first_index, num_dict[target - num].pop(0)]
    return []