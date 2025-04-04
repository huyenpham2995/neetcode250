from typing import List

def bubbleSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    
    return nums