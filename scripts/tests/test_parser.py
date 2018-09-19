import os
import sys
from typing import List

import pytest

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts import backend, frontend, scripts_test_runner, run
from scripts.utils import command_line
from scripts.utils.command_line import CommandOptionList


def parse_args(command_options: CommandOptionList, args: List[str]):
    parser = command_line.create_parser(command_options, description="")
    return parser.parse_args(args)


def assert_raises_parser_error(command_options: CommandOptionList, args: List[str]):
    parsed_args = parse_args(command_options, args)
    with pytest.raises(TypeError):
        command_line.execute_command(parsed_args, command_options)


def assert_backend_and_frontend_raise_error(args: List[str]):
    assert_raises_parser_error(command_options=backend.command_options, args=args)
    assert_raises_parser_error(command_options=frontend.command_options, args=args)


def test_dependency_management_requires_dependencies():
    assert_backend_and_frontend_raise_error(args=["add"])
    assert_backend_and_frontend_raise_error(args=["upgrade"])
    assert_backend_and_frontend_raise_error(args=["remove"])


def test_only_dependency_management_allows_variable_arguments():
    assert_backend_and_frontend_raise_error(args=["types", "bad"])
    assert_backend_and_frontend_raise_error(args=["run", "bad"])
    assert_backend_and_frontend_raise_error(args=["install", "bad"])


def test_help_works():
    def assert_no_error_raised(command_options: CommandOptionList) -> None:
        try:
            parse_args(command_options, ["--help"])
        except SystemExit as e:
            if e.code != 0:
                raise AssertionError from e

    assert_no_error_raised(run.command_options)
    assert_no_error_raised(backend.command_options)
    assert_no_error_raised(frontend.command_options)
    assert_no_error_raised(scripts_test_runner.command_options)
