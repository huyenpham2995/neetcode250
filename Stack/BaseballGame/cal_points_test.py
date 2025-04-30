import pytest
from cal_points import calPoints

def test():
    assert calPoints(["5","2","C","D","+"]) == 30
    assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27
    assert calPoints(["1","C"]) == 0