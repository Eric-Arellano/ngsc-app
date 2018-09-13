"""
Utilities to accept and parse command line arguments.
"""

import argparse
import functools
from typing import Any, Callable, List, NamedTuple, Optional, Union

NoArgCommand = Callable[[], None]
DependencyCommand = Callable[[List[str]], None]
Command = Union[NoArgCommand, DependencyCommand]


class CommandOption(NamedTuple):
    name: str
    command: Command
    help: Optional[str]


CommandOptionList = List[CommandOption]


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    pass


# -------------------------------------
# Command line arguments
# -------------------------------------

def create_parser(command_options: CommandOptionList, *,
                  description: str) -> argparse.ArgumentParser:
    """
    Setups command line argument parser and assigns defaults and help statements.

    See https://stackoverflow.com/a/49999185 for HelpFormatter code.
    """

    class HelpFormatterWithChoices(argparse.ArgumentDefaultsHelpFormatter):
        def add_argument(self, action: argparse.Action):
            if action.help is not argparse.SUPPRESS:
                if isinstance(action.choices, dict):
                    for choice, choice_help in action.choices.items():
                        self._add_item(self.format_choices, [choice, choice_help])
                else:
                    super().add_argument(action)

        def format_choices(self, choice, choice_help):
            # determine the required width and the entry label
            help_position = min(self._action_max_length + 2,
                                self._max_help_position)
            help_width = max(self._width - help_position, 11)
            action_width = help_position - self._current_indent - 2
            choice_header = choice

            # short choice name; start on the same line and pad two spaces
            if len(choice_header) <= action_width:
                tup = self._current_indent, '', action_width, choice_header
                choice_header = '%*s%-*s  ' % tup
                indent_first = 0

            # long choice name; start on the next line
            else:
                tup = self._current_indent, '', choice_header
                choice_header = '%*s%s\n' % tup
                indent_first = help_position

            # collect the pieces of the choice help
            parts = [choice_header]

            # add lines of help text
            help_lines = self._split_lines(choice_help, help_width)
            parts.append('%*s%s\n' % (indent_first, '', help_lines[0]))
            for line in help_lines[1:]:
                parts.append('%*s%s\n' % (help_position, '', line))

            # return a single string
            return self._join_parts(parts)

    parser = argparse.ArgumentParser(
            description=description,
            formatter_class=HelpFormatterWithChoices,
    )

    command_group = parser.add_argument_group(title='Possible commands')
    command_group.add_argument(
            'command',
            default='run',
            nargs='?',
            metavar='COMMAND',
            choices={option.name: option.help for option in command_options}
    )

    parser.add_argument('dependencies',
                        default='',
                        nargs='*',  # 0-many arguments
                        help='Dependency(ies) you want to modify.')

    return parser


def execute_command(args: argparse.Namespace,
                    command_options: CommandOptionList) -> None:
    """
    Determines which command was passed and then executes the command.

    Passes any additional parameters, such as target environment or dependencies.
    """
    command_map = {entry.name: entry.command for entry in command_options}
    func = command_map[args.command]
    # convert arguments to dict
    passed_arguments = vars(args)
    # remove empty values
    additional_arguments = {k: v for k, v in passed_arguments.items() if v}
    # remove command
    del additional_arguments['command']
    # unpack additional arguments into function as named parameters
    func(**additional_arguments)  # type: ignore


# -------------------------------------
# Interactive CLI
# -------------------------------------

def ask_input(prompt: str, *, is_valid: Callable[[str], bool] = None) -> str:
    """

    """
    print(prompt)
    result = input()
    if is_valid is not None and not is_valid(result):
        print('Invalid input.\n')
        return ask_input(prompt, is_valid=is_valid)
    return result


def ask_yes_no(question: str, *, default: str = 'yes') -> bool:
    """
    Ask given prompt and expect Y or N as answer.
    """
    options = {'yes': True, 'y': True, 'ye': True,
               'no': False, 'n': False}
    # determine prompt
    if default is None:
        prompt = '[y/n]'
    elif default == 'yes':
        prompt = '[Y/n]'
    elif default == 'no':
        prompt = '[y/N]'
    else:
        raise ValueError(f'invalid default answer: {default}')
    # ask prompt
    print(f'{question} {prompt}')
    # interpret result
    choice = input().lower()
    if default is not None and choice == '':
        return options[default]
    if choice in options:
        return options[choice]
    else:
        print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
        return ask_yes_no(question)


def ask_confirmation(instructions: str, *, default_to_yes: bool = False) -> None:
    """
    Ask for simple "yes" confirmation.
    """
    prompt = '[Y]' if default_to_yes else '[y]'
    options = ['yes', 'y', 'ye']
    print(f'{instructions}\n\nPlease confirm you have completed the above. {prompt}')
    # interpret result
    choice = input().lower()
    if choice not in options and not (default_to_yes and choice == ''):
        print("Please respond with 'yes' (or 'y').\n")
        return ask_confirmation(instructions)


def log(*, start_message: str = None, end_message: str = None) -> Callable[[Any], Any]:
    def decorate(func: Callable[[Any], Any]):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if start_message is not None:
                print(start_message)
            result = func(*args, **kwargs)
            if end_message is not None:
                print(end_message)
            return result

        return wrapper

    return decorate
