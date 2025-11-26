import unittest
from src.operazioni import somma, sottrai, dividi

class TestOperation(unittest.TestCase):
     def test_somma(self):
       assert somma(2, 3) == 5
       assert somma(-1, 1) == 0

     def test_sottrazioni(self):
       assert sottrai(10, 3) == 7
       assert sottrai(0, 5) == -5

     def test_dividi(self):
       assert dividi(10, 2) == 5
       assert dividi(9, 3) == 3

     def test_dividi_zero(self):
       with self.assertRaises(ValueError):
            dividi(5, 0)
            dividi(5, 0)

if __name__ == "__main__":
    unittest.main()