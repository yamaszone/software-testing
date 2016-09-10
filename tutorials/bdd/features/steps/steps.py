from behave import *
import subprocess
import pexpect

import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.PhantomJS()

@given(u'a Ubuntu development machine')
def step_impl(context):
    pass

@given(u'nose is installed')
def step_impl(context):
    pass

@given(u'coverage is installed')
def step_impl(context):
    pass

@when(u'I execute "{cmd}"')
def step_impl(context, cmd):
    out = execute(cmd)
    context.out = out

@then(u'I should see "{expected_text}"')
def step_impl(context, expected_text):
    assert expected_text in context.out

def execute(cmd):
    output, status = pexpect.run(cmd
                                 , withexitstatus=1
                                 , timeout=600
                                )

    return output

@given(u'I navigate to "{url}"')
def step_impl(context, url):
    driver.get(url)

@when(u'I search for "{keyword}"')
def step_impl(context, keyword):
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys(keyword)
    inputElement.submit()
    context.driver = driver

@then(u'I should see "{expected_text}" in the page title')
def step_impl(context, expected_text):
    WebDriverWait(context.driver, 10).until(EC.title_contains(expected_text))
