import pytest
from encode_and_decode import encode, decode

def testEmpty():
    assert encode([]) == ""
    assert decode("") == []

def test():
    assert encode(["neet","code","love","you"]) == "4#neet4#code4#love3#you"
    assert decode("4#neet4#code4#love3#you") == ["neet","code","love","you"]