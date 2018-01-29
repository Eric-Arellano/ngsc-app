from functools import partial
from typing import Callable, Dict, List
from unittest import TestCase, skip

import backend
import frontend
import helper


class ParserTester(TestCase):

    def assert_parser_error_thrown(self,
                                   command_map: Dict[str, Callable],
                                   error: Exception,
                                   args: List[str]):
        parser = helper.create_parser(backend.command_map)
        parsed_args = parser.parse_args(args)
        with self.assertRaises(error):
            helper.execute_command(parsed_args, command_map)


class TestSingleServerParser(ParserTester):

    def test_dependency_management_requires_dependencies(self):
        # backend
        backend_test = partial(self.assert_parser_error_thrown,
                               command_map=backend.command_map,
                               error=TypeError)
        backend_test(args=['add'])
        backend_test(args=['upgrade'])
        backend_test(args=['remove'])
        # frontend
        frontend_test = partial(self.assert_parser_error_thrown,
                                command_map=frontend.command_map,
                                error=TypeError)
        frontend_test(args=['add'])
        frontend_test(args=['upgrade'])
        frontend_test(args=['remove'])

    def test_only_dependency_management_allows_variable_arguments(self):
        # backend
        backend_test = partial(self.assert_parser_error_thrown,
                               command_map=backend.command_map,
                               error=TypeError)
        backend_test(args=['types', 'bad'])
        backend_test(args=['run', 'bad'])
        backend_test(args=['install', 'bad'])
        # frontend
        frontend_test = partial(self.assert_parser_error_thrown,
                                command_map=frontend.command_map,
                                error=TypeError)
        frontend_test(args=['types', 'bad'])
        frontend_test(args=['run', 'bad'])
        frontend_test(args=['install', 'bad'])


class TestRunParser(ParserTester):

    @skip
    def test_execute_on_target_environment_requires_target_action(self):
        raise NotImplementedError

    @skip
    def test_dependency_management_requires_target_specification(self):
        raise NotImplementedError

    @skip
    def test_dependency_management_requires_dependencies(self):
        raise NotImplementedError

    @skip
    def test_only_dependency_management_allows_variable_arguments(self):
        raise NotImplementedError
