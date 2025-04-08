import pytest
from product_of_array import productExceptSelf

def test_empty():
    assert productExceptSelf([]) == []

def test():
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]