from behave import *
import subprocess
import pexpect

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
