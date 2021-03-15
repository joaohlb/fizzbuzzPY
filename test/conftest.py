from pytest import fixture
from fizzbuzz import fizzbuzz

@fixture
def fizzbuzz100():
    return fizzbuzz(100)