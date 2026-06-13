import pytest
from calculator import add, subtract, multiply, divide


# --- add ---
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -4) == -5

def test_add_mixed():
    assert add(-3, 7) == 4

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_zero():
    assert add(0, 0) == 0


# --- subtract ---
def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_to_negative():
    assert subtract(2, 9) == -7

def test_subtract_zero():
    assert subtract(5, 0) == 5


# --- multiply ---
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(99, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 5) == -10

def test_multiply_two_negatives():
    assert multiply(-3, -3) == 9

def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0


# --- divide ---
def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_negative():
    assert divide(-9, 3) == -3.0

def test_divide_float_result():
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0

def test_divide_by_negative():
    assert divide(10, -2) == -5.0
