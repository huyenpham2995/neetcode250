import pytest
from majority_element import majorityElement2

def testOneElement():
    assert majorityElement2([1]) == [1]
    
def testNoElemet():
    assert majorityElement2([1,2,3]) == []
    
def test():
    assert majorityElement2([3,2,3]) == [3]
    assert majorityElement2([1,2]) == [1,2]