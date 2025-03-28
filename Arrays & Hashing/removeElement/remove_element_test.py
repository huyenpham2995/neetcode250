import pytest
from remove_element import removeElement

def testEmpty():
    assert removeElement([],0) == 0

def test():
    assert removeElement([3,2,2,3],3) == 2
    assert removeElement([0,1,2,2,3,0,4,2], 2) == 5
