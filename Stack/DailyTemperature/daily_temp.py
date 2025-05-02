from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        if not stack or temperatures[i] <= temperatures[i-1]:
            stack.append(i)
        else:
            j = i-1
            while stack:
                j = stack.pop(-1)
                if temperatures[i] > temperatures[j]:
                    res[j] = i-j
                else:
                    stack.append(j)
                    break
            stack.append(i)
    return res
