import pytest
from .calculator import add, subtract

@pytest.fixture
def calculator_setup():
    print("Setting up environment")
    return 

def test_add(calculator_setup):
    assert add(3,4) == 7

def test_subtract(calculator_setup):
    assert subtract(4,2) == 2