import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
CURRENT_FILE_PATH = Path(os.path.realpath(__file__))
sys.path.append(str(CURRENT_FILE_PATH.parents[1]))

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
