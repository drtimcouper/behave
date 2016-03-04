from behave import given, when, then

from nose.tools import assert_equal


@given('I am logged in')
def step_logged_in(context):
    pass


@when('I go to the root page')
def step_go_to_root(context):
   context.browser.get('http://localhost:5000/')


@then('I see title {title}')
def step_check_title(context, title):
    assert_equal(context.browser.title, title)
