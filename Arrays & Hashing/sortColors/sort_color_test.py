import pytest
from sort_color import sort_colors_count, sort_colors_three_pointers

def test_empty():
    assert sort_colors_count([]) == []
    assert sort_colors_three_pointers([]) == []

def test_valid():
    assert sort_colors_count([2,0,2,1,1,0]) == [0,0,1,1,2,2]
    assert sort_colors_three_pointers([2,0,2,1,1,0]) == [0,0,1,1,2,2]
    assert sort_colors_count([2,0,1]) == [0,1,2]
    assert sort_colors_three_pointers([2,0,1]) == [0,1,2]
    assert sort_colors_count([1,2,0]) == [0,1,2]
    assert sort_colors_three_pointers([1,2,0]) == [0,1,2]

    