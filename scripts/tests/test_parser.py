from typing import List

from scripts import run
from scripts.utils import command_line


def parse_args(args: List[str]):
    parser = command_line.create_parser(run.command_options, description="")
    return parser.parse_args(args)


def test_help_works():
    try:
        parse_args(["--help"])
    except SystemExit as error:
        if error.code != 0:
            raise AssertionError from error
