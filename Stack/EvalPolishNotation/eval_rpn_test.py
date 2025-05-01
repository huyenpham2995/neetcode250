import pytest
from eval_rpn import evalRPN

def test():
    assert evalRPN(["4","13","5","/","+"]) == 6
    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22