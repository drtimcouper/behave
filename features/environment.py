

from time import sleep
from multiprocessing import Process

from selenium import webdriver

from myapp import myapp
app = myapp.app

from behave import use_step_matcher

use_step_matcher("parse")


def before_all(context):
    context.browser = webdriver.Firefox()
    context.server = Process(target=app.run)
    context.server.start()
    sleep(1)


def after_all(context):
    context.server.terminate()
    context.server.join()
    context.browser.quit()
