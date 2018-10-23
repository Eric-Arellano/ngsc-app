from glob import glob

from scripts.utils import pipenv, sys_calls, command_line

# -------------------------------------
# Required software
# -------------------------------------


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    command_line.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    pipenv.check_prereqs_installed()


# -------------------------------------
# Test commands
# -------------------------------------


def green() -> None:
    """
    Call all tests and linters.
    """
    test()
    check_types()
    fmt()


def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    pipenv.run(
        [
            "mypy",
            "--strict-optional",
            "--ignore-missing-imports",
            "--package",
            "scripts",
        ]
    )


def test() -> None:
    """
    Run unit tests.
    """
    pipenv.run(["pytest", "-q"], cwd="scripts")


def fmt() -> None:
    """
    Auto-formats script code.
    """
    targets_from_root = glob("scripts/**/*.py", recursive=True)
    pipenv.run(["black", "--py36"] + targets_from_root)


# -------------------------------------
# Command line options
# -------------------------------------


def create_command_option(
    name: str, command: command_line.Command
) -> command_line.CommandOption:
    return command_line.CommandOption(name=name, command=command, help=command.__doc__)


command_options = [
    create_command_option("green", green),
    create_command_option("test", test),
    create_command_option("types", check_types),
    create_command_option("fmt", fmt),
]
