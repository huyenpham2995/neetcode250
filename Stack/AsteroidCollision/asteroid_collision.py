from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for a in asteroids:
        add = True
        while stack and a<=stack[-1] and a*stack[-1] < 0:
            if abs(a) > abs(stack[-1]):
                stack.pop(-1)
            else:
                add = False
                if abs(a) == abs(stack[-1]):
                    stack.pop(-1)
                break
        if add:
            stack.append(a)
    return stack
