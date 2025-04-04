from typing import List

def quickSortRecursion(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    pivot = nums[0]
    left_arr = [num for num in nums[1:] if num <= pivot]
    right_arr = [num for num in nums[1:] if num > pivot]

    return sortArray(left_arr) + [pivot] + sortArray(right_arr)