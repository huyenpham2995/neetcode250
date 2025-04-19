import pytest
from max_profit import maxProfit

def testZero():
    assert maxProfit([7,6,4,3,1]) == 0
    
def testMaxProfit():
    assert maxProfit([7,1,5,3,6,4]) == 7
    assert maxProfit([1,2,3,4,5]) == 4