import pytest
from anagram_group1 import groupAnagrams1
from anagram_group2 import groupAnagrams2

def testEmpty():
    assert groupAnagrams1([""]) == [[""]]
    assert groupAnagrams2([""]) == [[""]]
    
def testSingle():
    assert groupAnagrams1(["a"]) == [["a"]]
    assert groupAnagrams2(["a"]) == [["a"]]

def testAnagramGroup():
    assert groupAnagrams1(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert groupAnagrams2(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
