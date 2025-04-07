from typing import List

def sort_colors_count(nums: List[int]) -> List:
    zero = one = two = 0
    for num in nums:
        if num == 0:
            zero += 1
        elif num == 1:
            one += 1
        else:
            two += 1
    i = 0
    while zero > 0:
        nums[i] = 0
        zero -= 1
        i += 1
    while one > 0:
        nums[i] = 1
        one -= 1
        i += 1
    while two > 0:
        nums[i] = 2
        two -= 1
        i += 1
    return nums
        
def sort_colors_three_pointers(nums: List[int]) -> List:
    cur = s_pointer = 0
    l_pointer = len(nums)-1

    while cur <= l_pointer:
        if nums[cur] == 0:
            nums[cur], nums[s_pointer] = nums[s_pointer], nums[cur]
            s_pointer += 1
        elif nums[cur] == 2:
            nums[cur], nums[l_pointer] = nums[l_pointer], nums[cur]
            l_pointer -= 1
            cur -= 1
        cur += 1
    return nums