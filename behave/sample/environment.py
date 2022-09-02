from os import environ

from behave.model import Feature, Scenario, Step
from behave.runner import Context


def before_all(context: Context):
    print(context.config.userdata.get("custom_value"))
    print(context.config.userdata.get("custom_value_1", "No value found"))


def before_feature(context: Context, feature: Feature):
    ...


def before_scenario(context: Context, scenario: Scenario):
    ...


def before_step(context: Context, step: Step):
    ...


def after_step(context: Context, step: Step):
    # Update here to avoid stuck tests
    if environ.get('DEBUG', True) and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_scenario(context: Context, scenario: Scenario):
    ...


def after_feature(context: Context, feature: Feature):
    ...


def after_all(context: Context):
    ...
