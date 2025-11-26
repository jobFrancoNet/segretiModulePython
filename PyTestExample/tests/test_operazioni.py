import pytest
from src.operazioni import somma, sottrai, dividi

def test_somma():
    assert somma(2, 3) == 5
    assert somma(-1, 1) == 0

def test_sottrai():
    assert sottrai(10, 3) == 7
    assert sottrai(0, 5) == -5

def test_dividi():
    assert dividi(10, 2) == 5
    assert dividi(9, 3) == 3

def test_dividi_zero():
    with pytest.raises(ValueError):
        dividi(5, 0)