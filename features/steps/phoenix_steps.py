import subprocess
from behave import given, when, then

PHONE_NUMBER = None
RESULT_STDOUT = None
RESULT_STDERR = None
EXIT_CODE = None

@given('I have the phone number "{phone_number}"')
def step_given_phone_number(context, phone_number):
    global PHONE_NUMBER
    PHONE_NUMBER = phone_number

@when('I run phonex with this phone number')
def step_run_phonex(context):
    global PHONE_NUMBER, RESULT_STDOUT, RESULT_STDERR, EXIT_CODE
    cmd = ['phonex', PHONE_NUMBER]
    process = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    RESULT_STDOUT = process.stdout
    RESULT_STDERR = process.stderr
    EXIT_CODE = process.returncode

@when('I run phonex with the \'{option}\' option')
def step_run_phonex_help(context, option):
    global RESULT_STDOUT, RESULT_STDERR, EXIT_CODE
    cmd = ['phonex', option]
    process = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    RESULT_STDOUT = process.stdout
    RESULT_STDERR = process.stderr
    EXIT_CODE = process.returncode

@then('it should generate multiple search variants')
def step_check_multiple_variants(context):
    assert "Opening Google search results for" in RESULT_STDOUT

@then('it should not show an error')
def step_no_error(context):
    assert EXIT_CODE == 0
    assert RESULT_STDERR.strip() == ""

@then('it should reject the phone number')
def step_reject_phone_number(context):
    assert EXIT_CODE == 1

@then('it should print an error that a prefix is required')
def step_print_prefix_error(context):
    assert "prefix" in (RESULT_STDOUT + RESULT_STDERR).lower()

@then('it should print an error that the phone number is invalid')
def step_print_invalid_error(context):
    assert "not a valid phone number" in (RESULT_STDOUT + RESULT_STDERR).lower()
    assert EXIT_CODE == 1

@then('it should print usage information')
def step_print_usage(context):
    assert "Usage:" in RESULT_STDOUT
    assert EXIT_CODE == 0

@given(u'I run phonex with the \'-h\' option')
def step_impl(context):
    global RESULT_STDOUT, RESULT_STDERR, EXIT_CODE
    cmd = ['phonex', '-h']
    process = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    RESULT_STDOUT = process.stdout
    RESULT_STDERR = process.stderr
    EXIT_CODE = process.returncode

