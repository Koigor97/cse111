from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Samuel", "Turay") == "Turay;Samuel"
    assert extract_family_name("Turay; Samuel") == "Turay"
    assert extract_given_name("Turay; Samuel") == "Samuel"


pytest.main(["-v", "--tb=line", "-rN", __file__])
