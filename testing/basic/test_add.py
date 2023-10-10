import pytest
import add_func

@pytest.mark.add
def test_add():
    result=(add_func.add(10,8) == 18)
    assert result

@pytest.mark.sub
def test_subtract():
    result=(add_func.subtract(10,8) == 2)
    assert result

@pytest.mark.mul
def test_multiply():
    result=(add_func.multiply(10,8) == 80)
    assert result
    #pytest -m mul