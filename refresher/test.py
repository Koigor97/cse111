import unittest
import pytest

from main import do_stuff

class TestMain:
    def test_do_stuff(self):
        test_param = 10
        assert do_stuff(num=test_param) == 100



