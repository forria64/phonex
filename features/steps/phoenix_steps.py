from behave import given, when, then
import subprocess

given_phone_number = None
result_stdout = None
result_stderr = None
exit_code = None

@given('I have the phone number "{phone_number}"')
def step_given_phone_number(context, phone_number):
    global given_phone_number
    given_phone_number = phone_number

@when('I run phonex with this phone number')
def step_run_phonex(context):
    global result_stdout, result_stderr, exit_code
    cmd = ['phonex', given_phone_number]
    process = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    result_stdout = process.stdout
    result_stderr = process.stderr
    exit_code = process.returncode

@then('it should generate multiple search variants')
def step_generate_variants(context):
    assert "Opening Google search results for" in result_stdout

@then('it should not show an error')
def step_no_error(context):
    assert exit_code == 0
    assert result_stderr.strip() == ""

@then('it should reject the phone number')
def step_reject_phone_number(context):
    assert exit_code == 1
    assert "error" in (result_stdout + result_stderr).lower()

@then('it should print an error that a prefix is required')
def step_prefix_error(context):
    assert "prefix" in (result_stdout + result_stderr).lower()

@then('it should print an error that the phone number is invalid')
def step_invalid_number_error(context):
    assert "not a valid phone number" in (result_stdout + result_stderr).lower()

@given('I run phonex with the \'-h\' option')
def step_run_help_option(context):
    global result_stdout, result_stderr, exit_code
    cmd = ['phonex', '-h']
    process = subprocess.run(cmd, capture_output=True, text=True)
    result_stdout = process.stdout
    result_stderr = process.stderr
    exit_code = process.returncode

@then('it should print usage information')
def step_usage_info(context):
    assert "Usage:" in result_stdout
    assert exit_code == 0

