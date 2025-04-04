from typing import List

def bubbleSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        swapped = False
        for j in range (len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums