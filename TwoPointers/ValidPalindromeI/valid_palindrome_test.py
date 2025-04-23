import pytest
from valid_palindrome import isPalindrome

def testAlphanum():
    assert isPalindrome("0P") == False

def testEmpty():
    assert isPalindrome(" ") == False

def test():
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False