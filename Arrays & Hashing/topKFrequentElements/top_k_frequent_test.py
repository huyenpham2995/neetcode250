import pytest
from top_k_frequent import topKFrequent

def testEmpty():
    assert topKFrequent([],0) == []

def testKLargerThanNum():
    assert topKFrequent([1,1,2],3) == [1,2]

def test():
    assert topKFrequent([1,1,1,2,2,3],2) == [1,2]
    assert topKFrequent([1],1) == [1]