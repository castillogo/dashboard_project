import re
import pytest
import requests
from bs4 import BeautifulSoup as soup
from number_code import add_one, squares_number, square_root_number

# how can i be sure that this test is comprehensive?
# why don't we think about edge cases
# what is the edge case of numbers? - highest possible positive integers, highest negative integers, zero, complex numbers, floats
def test_add_postivie_one():
    assert add_one(10) == 11

def test_add_negative_one():
    assert add_one(-10) == -9

def test_add_zero():
    assert add_one(0) == 1

# why don't we run all these tests in one function
# we can do this with parameterized test functions

# we need a set of inputs
# and we need to define the decorator
PASSING_CONDITIONS = [(10,11), (-10,-9), (0,1), (1,2)]
@pytest.mark.parametrize(["input", "output"], PASSING_CONDITIONS)
def test_one_set_of_additions(input, output):
    assert add_one(input) == output


#Integration testing example
# edge case for the integration
def test_integration():
    assert squares_number(add_one(2)) == 9

# test for a specific error
def test_non_square_rootable_input():
    with pytest.raises(Exception):
        square_root_number(add_one(-2))


@pytest.fixture
def scraper():
    http_response = requests.get('http://www.metrolyrics.com/rihanna-lyrics.html')
    parse_text = soup(http_response.text, 'html.parser')
    return parse_text

#first example i showed
def test_connection_sucessful(scraper):
    assert len(scraper()) > 0
