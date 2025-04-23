import pytest
from reverse_string import reverseString

def testEmpty():
    assert reverseString([]) == []
    
def test():
    assert reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
    assert reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]

