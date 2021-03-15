from fizzbuzz import fizzbuzz
import pytest

def test_invalid():
    with pytest.raises(ValueError):
        fizzbuzz('abc')

def test_100_elements(fizzbuzz100):
    expected = 100
    result = len(fizzbuzz100)
    assert result == expected

def test_1st_fizzbuzz_element(fizzbuzz100):
    expected = 1
    result = fizzbuzz100[0]
    assert result == expected

def test_3rd_fizzbuzz_element(fizzbuzz100):
    expected = 'Fizz'
    result = fizzbuzz100[2]
    assert result == expected

def test_5th_fizzbuzz_element(fizzbuzz100):
    expected = 'Buzz'
    result = fizzbuzz100[4]
    assert result == expected

def test_15th_fizzbuzz_element(fizzbuzz100):
    expected = 'FizzBuzz'
    result = fizzbuzz100[14]
    assert result == expected