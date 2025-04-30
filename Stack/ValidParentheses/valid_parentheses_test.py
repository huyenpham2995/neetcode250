import pytest
from valid_parentheses import isValid

def testValid():
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("([])") == True
    
def testInvalid():
    assert isValid("(]") == False
    assert isValid("[") == False
    assert isValid("}") == False