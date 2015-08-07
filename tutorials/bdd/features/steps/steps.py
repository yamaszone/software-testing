from behave import *
import subprocess


@given(u'nose is installed')
def step_impl(context):
    pass
 
@when(u'I execute "{cmd}"')
def step_impl(context, cmd):
    p = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = p.communicate()
    context.out = out

@then(u'I should see "{expected_text}"')
def step_impl(context, expected_text):
    assert expected_text in context.out


