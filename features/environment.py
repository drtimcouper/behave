

from time import sleep
from multiprocessing import Process

from selenium import webdriver

from myapp import myapp
app = myapp.app


def before_all(context):
    context.browser = webdriver.Firefox()
   # context.myapp = myapp
    context.server = Process(target=app.run)
    context.server.start()
    sleep(2)


def after_all(context):
    context.server.terminate()
    context.server.join()
    #context.myapp.shutdown_server()
    context.browser.quit()
