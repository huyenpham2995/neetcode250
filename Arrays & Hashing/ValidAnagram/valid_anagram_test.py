import pytest
from valid_anagram import isAnagram

def testEmpty():
    assert isAnagram("","") == True

def testUnequalLength():
    assert isAnagram("abc","ab") == False
    
def testAnagram():
    assert isAnagram("anagram","nagaram") == True
    assert isAnagram("rat","car") == False