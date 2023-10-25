from w1_sample import miles_per_gallon, lp100k_from_mpg
from pytest import approx
import pytest


class TestFunctions:

    def test_miles_per_gallon(self):
        assert miles_per_gallon(70, 112, 11) == approx(3.8)

    def test_lp100k_from_mpg(self):
        assert lp100k_from_mpg(3.8) == approx(61.9)


pytest.main(["-v", "--tb=no", "test_w3_w1_sample.py"])
