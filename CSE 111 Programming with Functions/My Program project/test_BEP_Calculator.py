from Function_place import total_in_list, break_even_point
from pytest import approx
from tkinter import *
import pytest

def test_total_in_list ():
    assert total_in_list ([2, 5, 7, 9]) == approx(23)
    assert total_in_list ([3, 73, 79, 45]) == approx(200)
    assert total_in_list ([6, 34, 0, 12]) == approx(52)
    assert total_in_list ([8, 4, 63, 79]) == approx(154)
    assert total_in_list ([9, 8, 6, 6]) == approx(29)

def test_break_even_point ():
    assert break_even_point (600, 10, 7) == approx(200)
    assert break_even_point (700, 30, 20) == approx(70)
    assert break_even_point (1000, 50, 45) == approx(200)
    assert break_even_point (5, 2, 1) == approx(5)
    assert break_even_point (4000, 50, 30) == approx(200)

pytest.main(["-v", "--tb=line", "-rN", __file__])

