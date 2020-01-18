import unittest_cases.mathlib as mathlib
import pytest

def test_calc_total():
    total = mathlib.calc_total(10,20)
    assert total == 30

def test_calc_multipy():
    multipy = mathlib.calc_multipy(10,20)
    assert multipy == 200

"""
Skip test
"""
@pytest.mark.skip(reason='I don"t want to test as of now')
def test_calc_total_v2():
    total = mathlib.calc_total(10,20)
    assert total == 30

"""
Skip test with condition as skip the test if python version is greater than 3.5
"""
import sys
@pytest.mark.skipif(sys.version_info >(3,5), reason='I don"t want to test as of now')
def test_calc_total_v3():
    total = mathlib.calc_total(10,20)
    assert total == 30


@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True
