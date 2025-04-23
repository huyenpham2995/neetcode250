import pytest
from merge_alternatively import mergeAlternately

def testEmpty():
    assert mergeAlternately("","ab") == "ab"
    assert mergeAlternately("bc","") == "bc"
    
def testEqualLength():
    assert mergeAlternately("abc","pqr") == "apbqcr"
    
def testUnequalLength():
    assert mergeAlternately("ab","pqrs") == "apbqrs"
    assert mergeAlternately("abcd","pq") == "apbqcd"