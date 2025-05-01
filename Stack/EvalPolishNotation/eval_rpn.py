from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    
    for t in tokens:
        if t == "*" or t == "/" or t == "+" or t == "-":
            num1 = stack.pop(0)
            num2 = stack.pop(0)
            
            if t == "*":
                stack.insert(0, num1*num2)
            elif t == "/":
                stack.insert(0, int(num2/num1))
            elif t == "+":
                stack.insert(0, num1+num2)
            else:
                stack.insert(0, num2-num1)
        else:
            stack.insert(0, int(t))
    return stack[0]
    