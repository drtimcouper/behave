from behave import given, when, then
from nose.tools import assert_equal


@given('I am logged in')
def step(context):
    context.browser.get('http://127.0.0.1:5000')


@when('I go to the root page')
def step(context):
    pass


@then('I see the title "Achtung Minen"')
def step(context):
    assert_equal(context.browser.title, "Achtung Minen")
