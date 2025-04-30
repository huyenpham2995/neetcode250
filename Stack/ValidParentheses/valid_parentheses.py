def isValid(s: str) -> bool:
    open_set = ('(', '[', '{')
    parentheses_dict = {'(':')', '{':'}', '[':']'}
    stack = []

    for p in s:
        if p in open_set:
            stack.insert(0,p)
        else:
            if len(stack) < 1:
                return False
            top = stack.pop(0)
            if parentheses_dict[top] != p:
                return False
    if len(stack) > 0:
        return False
    return True