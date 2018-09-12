#!/usr/bin/env python3.7

"""
Top level script to install, run, test, deploy, update, and manage dependencies
for the whole app and its backend and frontend.

Commands follow the syntax:
    `./run.py [command] [-t target]`, where
        [target] = [all|backend|frontend|script] with default to `all`
        [command] = one of the valid commands with default to `run`

Usage:
    run...
            run (detached): `./run.py [--backend|frontend]`
            stop: `./run.py stop [--backend|frontend]`
    install...
            install: `./run.py install [--backend|frontend]`
            reinstall: ./run.py reinstall [--backend|frontend]`
    test...
            run tests: `./run.py test [--backend|scripts]`
            check types: `./run.py types [--backend|frontend]`
    dependency management...
            view outdated: `./run.py outdated [--backend|frontend]`
            add: `./run.py add package1 [package2..] --backend|frontend`
            upgrade: `./run.py upgrade package1 [package2..] --backend|frontend`
            remove: `./run.py remove package1 [package2..] --backend|frontend`
    deploy...
            deploy: `./run.py deploy`
    update student info...
            update: `./run.py student-info`
"""
import os
import sys
from pathlib import Path

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
current_file_path = Path(os.path.realpath(__file__))
sys.path.append(str(current_file_path.parents[1]))

import argparse
from functools import partial
from typing import List, NamedTuple, Iterator, Optional

from scripts import backend, deploy, frontend, scripts_test_runner, update_demographics
from scripts.utils import command_line, pipenv


def main() -> None:
    parser = command_line.create_parser(
            command_map,
            description='Top level script to install, run, test, deploy, update, and manage dependencies '
                        'for the whole app and its backend and frontend.'
    )
    add_targets_to_parser(parser)
    args = parser.parse_args()
    check_prereqs()
    pipenv.remove_old_venv()
    command_line.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    backend.check_prereqs()
    frontend.check_prereqs_installed()
    deploy.check_prereqs_installed()
    update_demographics.check_prereqs_installed()
    scripts_test_runner.check_prereqs_installed()
    command_line.check_prereqs_installed()


# -------------------------------------
# Determine target environment
# -------------------------------------

class TargetCommandMap(NamedTuple):
    all_action: Optional[command_line.Command] = None
    backend_action: Optional[command_line.Command] = None
    frontend_action: Optional[command_line.Command] = None
    scripts_action: Optional[command_line.Command] = None
    has_dependencies: bool = False


def add_targets_to_parser(parser: argparse.ArgumentParser) -> None:
    def add_arg(abbreviation: str, full_name: str):
        parser.add_argument(abbreviation, full_name, action='store_true',
                            help=f"Operate on {full_name.replace('--', '')} specifically.")

    add_arg('-b', '--backend')
    add_arg('-f', '--frontend')
    add_arg('-s', '--scripts')


def raise_invalid_target(target_command_map: TargetCommandMap) -> None:
    target_names = {
        '--all (default)': target_command_map.all_action,
        '--backend': target_command_map.backend_action,
        '--frontend': target_command_map.frontend_action,
        '--scripts': target_command_map.scripts_action
    }
    supported_targets = '\n'.join(
            [target_name for target_name, action in target_names.items() if action is not None]
    )
    raise SystemExit(f'Invalid target. This command supports the following targets:\n{supported_targets}')


def execute_on_target_environment(target_command_map: TargetCommandMap, *,
                                  backend: bool = False,
                                  frontend: bool = False,
                                  scripts: bool = False,
                                  dependencies: List[str] = None) -> None:
    # check valid targets
    target_specified = backend or frontend or scripts
    invalid_all = not target_specified and target_command_map.all_action is None
    invalid_backend = backend and target_command_map.backend_action is None
    invalid_frontend = frontend and target_command_map.frontend_action is None
    invalid_scripts = scripts and target_command_map.scripts_action is None
    if any((invalid_all, invalid_backend, invalid_frontend, invalid_scripts)):
        raise_invalid_target(target_command_map)

    # default to all
    if not target_specified:
        target_command_map.all_action()  # type: ignore
        return

    # find every target specified
    commands = [
        target_command_map.backend_action if backend else None,
        target_command_map.frontend_action if frontend else None,
        target_command_map.scripts_action if scripts else None
    ]
    filtered_commands: Iterator[command_line.Command] = filter(None, commands)

    # check if dependencies
    kwargs = {}
    if target_command_map.has_dependencies:
        kwargs['dependencies'] = dependencies

    # execute
    for command in filtered_commands:
        command(**kwargs)  # type: ignore


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> TargetCommandMap:
    """
    Runs app in detached mode.
    """

    def all_action() -> None:
        backend.run_detached()
        frontend.run_detached()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.run,
            frontend_action=frontend.run
    )


def stop() -> TargetCommandMap:
    """
    Stops detached servers on specified target environment.
    """

    def all_action() -> None:
        backend.stop()
        frontend.stop()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.stop,
            frontend_action=frontend.stop
    )


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> TargetCommandMap:
    """
    Install everything needed for the app to function.
    """

    def all_action() -> None:
        backend.install()
        frontend.install()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.install,
            frontend_action=frontend.install
    )


def reinstall() -> TargetCommandMap:
    """
    Deletes original packages and re-installs everything.
    """

    def all_action() -> None:
        backend.reinstall()
        frontend.reinstall()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.reinstall,
            frontend_action=frontend.reinstall
    )


# -------------------------------------
# Test commands
# -------------------------------------

def green() -> TargetCommandMap:
    """
    Call all tests and linters.
    """

    def all_action() -> None:
        backend.green()
        frontend.green()
        scripts_test_runner.green()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.green,
            frontend_action=frontend.green,
            scripts_action=scripts_test_runner.green
    )


def test() -> TargetCommandMap:
    """
    Run unit tests for specified environment.
    """

    def all_action() -> None:
        backend.test()
        frontend.test()
        scripts_test_runner.test()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.test,
            frontend_action=frontend.test,
            scripts_action=scripts_test_runner.test
    )


def check_types() -> TargetCommandMap:
    """
    Call Flow and MyPy to check type safety of app.
    """

    def all_action() -> None:
        backend.check_types()
        frontend.check_types()
        scripts_test_runner.check_types()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.check_types,
            frontend_action=frontend.check_types,
            scripts_action=scripts_test_runner.check_types
    )


# -------------------------------------
# Dependency management commands
# -------------------------------------


def list_outdated() -> TargetCommandMap:
    """
    List packages that should be updated.
    """

    def all_action() -> None:
        backend.list_outdated()
        frontend.list_outdated()

    return TargetCommandMap(
            all_action=all_action,
            backend_action=backend.list_outdated,
            frontend_action=frontend.list_outdated
    )


def dependency_tree() -> TargetCommandMap:
    """
    Visualize which dependencies depend upon each other.
    """
    return TargetCommandMap(
            all_action=backend.dependency_tree,
            backend_action=backend.dependency_tree
    )


def add() -> TargetCommandMap:
    """
    Add one or more packages.
    """
    return TargetCommandMap(
            backend_action=backend.add,
            frontend_action=frontend.add,
            has_dependencies=True
    )


def upgrade() -> TargetCommandMap:
    """
    Upgrade one or more out-of-date packages.
    """
    return TargetCommandMap(
            backend_action=backend.upgrade,
            frontend_action=frontend.upgrade,
            has_dependencies=True
    )


def remove() -> TargetCommandMap:
    """
    Remove one or more packages.
    """
    return TargetCommandMap(
            backend_action=backend.remove,
            frontend_action=frontend.remove,
            has_dependencies=True
    )


# -------------------------------------
# Deploy commands
# -------------------------------------

def deploy_to_heroku() -> TargetCommandMap:
    """
    Push changes to GitHub and Heroku.
    """
    return TargetCommandMap(all_action=deploy.main)


# -------------------------------------
# Update student info commands
# -------------------------------------

def update_student_info() -> TargetCommandMap:
    """
    Check for changes to hardcoded student information and then commit changes.
    """
    return TargetCommandMap(all_action=update_demographics.main)


# -------------------------------------
# Setup new semester's Drive
# -------------------------------------

def setup_semester() -> TargetCommandMap:
    """
    Create the new Google Drive for upcoming semester, e.g. preparing rosters and copying files.
    """

    def run_script() -> None:
        pipenv.run([
            'python',
            './backend/src/admin/new_semester_scripts/setup_semester.py'
        ])

    return TargetCommandMap(all_action=run_script)


def share_drive() -> TargetCommandMap:
    """
    Share the new Google Drive with incoming student leadership.
    """

    def run_script() -> None:
        pipenv.run([
            'python',
            './backend/src/admin/new_semester_scripts/share_drive.py'
        ])

    return TargetCommandMap(all_action=run_script)


def rebuild_rosters() -> TargetCommandMap:
    """
    Rebuild the rosters with updated student info. Overwrites current data.
    """

    def run_script() -> None:
        pipenv.run([
            'python',
            './backend/src/admin/new_semester_scripts/rebuild_rosters.py'
        ])

    return TargetCommandMap(all_action=run_script)


# -------------------------------------
# Command line options
# -------------------------------------

def support_targets(command):
    return partial(execute_on_target_environment, command())


command_map = command_line.CommandMap({
    'run': support_targets(run),
    'stop': support_targets(stop),
    'install': support_targets(install),
    'reinstall': support_targets(reinstall),
    'green': support_targets(green),
    'test': support_targets(test),
    'types': support_targets(check_types),
    'outdated': support_targets(list_outdated),
    'deptree': support_targets(dependency_tree),
    'add': support_targets(add),
    'upgrade': support_targets(upgrade),
    'remove': support_targets(remove),
    'deploy': support_targets(deploy_to_heroku),
    'student-info': support_targets(update_student_info),
    'setup-semester': support_targets(setup_semester),
    'share-drive': support_targets(share_drive),
    'rebuild-rosters': support_targets(rebuild_rosters)
})

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()
