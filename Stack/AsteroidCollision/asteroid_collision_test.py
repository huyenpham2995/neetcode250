import pytest
from asteroid_collision import asteroidCollision

def test():
    assert asteroidCollision([5,10,-5]) == [5,10]
    assert asteroidCollision([8,-8]) == []
    assert asteroidCollision([10,2,-5]) == [10]
    assert asteroidCollision([-2,-2,-2,-2]) == [-2,-2,-2,-2]