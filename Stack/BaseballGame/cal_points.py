import re
from typing import List
    
def calPoints(operations: List[str]) -> int:
    stack = []

    for item in operations:
        if item == 'C':
            stack.pop(0)
        else:
            i = 0
            if item == '+':
                i = stack[0] + stack[1]
            elif item == 'D':
                i = 2*stack[0]
            else:
                i = int(item)
            stack.insert(0,i)
    return sum(stack)