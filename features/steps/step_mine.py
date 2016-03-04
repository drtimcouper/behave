from behave import given, when, then

from nose.tools import assert_equal, assert_in

import logging

logger = logging.getLogger()

@given('I am logged in')
def step_logged_in(context):
    pass


@when('I go to the root page')
def step_go_to_root(context):
   context.browser.get('http://localhost:5000/')


@then('I see title {title}')
def step_check_title(context, title):
    assert_equal(context.browser.title, title)


@then('I see user {name} in the page')
def step_see_user(context, name):
    el = context.browser.find_element_by_tag_name("body")
    assert_in(name, el.text)



