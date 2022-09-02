import parse
from behave import step, register_type
from behave.runner import Context
from requests import get


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)


@step('fetch data from "{url}"')
def fetch_url_data(context: Context, url: str):
    response = get(url)
    context.response = response


@step('response status code is {status_code:Number}')
def fetch_url_data(context: Context, status_code: int):
    assert context.response.status_code == status_code
