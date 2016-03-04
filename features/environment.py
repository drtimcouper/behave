from time import sleep
from multiprocessing import Process

from selenium import webdriver

from myapp import myapp

from behave import use_step_matcher

use_step_matcher("parse")


def before_all(context):
    context.myapp = myapp
    context.server = Process(target=context.myapp.app.run)
    context.server.start()
    sleep(1)


def after_all(context):
    context.server.terminate()
    context.server.join()


def before_scenario(context, scenario):
    context.browser = webdriver.Firefox()


def after_scenario(context, scenario):
    context.browser.quit()
