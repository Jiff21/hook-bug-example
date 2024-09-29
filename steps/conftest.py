'''Using Conftest.py as as the behave equivalent of common.py'''
import pytest
import requests
from steps.environment import context
from pytest_bdd import scenario, given, when, then, parsers, scenarios

class Style():
  RED = "\033[31m"
  RESET = "\033[0m"

############
# Test Hooks
############

def pytest_sessionstart(session):
    # print('\nBefore All Hook:\n')
    pass


def pytest_sessionfinish(session, exitstatus):
    # print('\nAfter All Hook:\n')
    pass


# Before and After Feature Hooks
# @pytest.fixture(scope="function", autouse=True)
# def after_feature_teardown_function(request):
#     print("\nBefore Feature Hook...function scope\n")
#     yield True
#     print("\nAfter Feature Hook...function scope\n")

@pytest.fixture(scope="class", autouse=True)
def after_feature_teardown_client(request):
    print("\nBefore Feature Hook...class scope.  Running before and after all scenario\n")
    yield True
    print("\nAfter Feature Hook...class scope. Running before and after all scenario\n")

@pytest.fixture(scope="module", autouse=True)
def after_feature_teardown_module(request):
    print("\nBefore Feature Hook...module scope. It's running before and after all features.\n")
    yield True
    print("\nAfter Feature Hook...module scope. It's running before and after all features\n")


# @pytest.fixture(scope="package", autouse=True)
# def after_feature_teardown_package(request):
#     print("\nBefore Feature Hook...package scope\n")
#     yield True
#     print("\nAfter Feature Hook...package scope\n")

# @pytest.fixture(scope="module", autouse=True)
# def after_feature_teardown_session(request):
#     print("\nBefore Feature Hook...session scope\n")
#     yield True
#     print("\nAfter Feature Hook...session scope\n")




# Before Scanrio Hook
def pytest_bdd_before_scenario(request, feature, scenario):
    print("Before Scenario Hook from {} Feature File".format(feature.name))
    # Print Scenario as it runs
    print('\n\nScenario: {scenario.name}'.format(scenario=scenario))


# After Scenario Hook
def pytest_bdd_after_scenario(request, feature, scenario):
    # print('\nAfter Scenario Hook\n')
    pass

# Before Step Hook
def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    # Print steps as they run
    # print('    {step.keyword} {step.name}'.format(keyword=step.keyword, step=step), end="", flush=True)
    pass

# After step passed or skipping hook
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    # Logic for live print if step passed
    # print(' - PASSED')
    pass

# After step failed hook
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # Logic for live print if step failed or not
    # print(f'{Style.RED} - FAILED{Style.RESET}')
    pass

##############
# Shared Steps
##############



@given(parsers.parse("I get the {page_name} using requests"))
@when(parsers.parse("I get the {page_name} using requests"))
def get_with_requests(context, page_name):
    pass
@then('the response should be successful')
def response_succeeded(context):
   pass

@given(parsers.parse("I get the {page_name} page"))
@when(parsers.parse("I get the {page_name} page"))
def get(context, page_name):
    pass
@then(parsers.parse('I should be on {expected_page}'))
def assert_page(context, expected_page):
    pass

@when('I check the console logs')
def check_console(context):
    pass


@then('there should be no severe console log errors')
def check_no_severe_errors(context):
    pass