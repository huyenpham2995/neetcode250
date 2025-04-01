import pytest
from majority_element import majorityElement1, majorityElement2, majorityElementBest

def test():
    assert majorityElement1([3,2,3]) == 3
    assert majorityElement2([3,2,3]) == 3
    assert majorityElementBest([3,2,3]) == 3
    assert majorityElement1([2,2,1,1,1,2,2]) == 2
    assert majorityElement2([2,2,1,1,1,2,2]) == 2
    assert majorityElementBest([2,2,1,1,1,2,2]) == 2
