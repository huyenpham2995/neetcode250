import pytest
from two_integer_sum_sol1 import twoSum1
from two_integer_sum_sol2 import twoSum2
from two_integer_sum_best import twoSumBest

def testPositive():
    assert twoSum1([2,7,11,15],9) == [0,1]
    assert twoSum2([2,7,11,15],9) == [0,1]
    assert twoSumBest([2,7,11,15],9) == [0,1]
    assert twoSum1([3,2,4],6) == [1,2]
    assert twoSum2([3,2,4],6) == [1,2]
    assert twoSumBest([3,2,4],6) == [1,2]
    
def testNegative():
    assert twoSum1([-2,7,-11,10], -4) == [1,2]
    assert twoSum2([-2,7,-11,10], -4) == [1,2]
    assert twoSumBest([-2,7,-11,10], -4) == [1,2]
    
def testDuplicate():
    assert twoSum1([3,3],6) == [0,1]
    assert twoSum2([3,3],6) == [0,1]
    assert twoSumBest([3,3],6) == [0,1] 