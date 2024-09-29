'''An Example test using Selenium browser.'''
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('features')

def test_all_tests_in_features():
    pass
