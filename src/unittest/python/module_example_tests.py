from mockito import mock, verify
import unittest

from module_example import hello_module


class ModuleExampleTest(unittest.TestCase):
    # noinspection PyMethodMayBeStatic
    def test_module_should_issue_hello_world_message(self):
        out = mock()

        hello_module(out)

        verify(out).write("Hello world from python module\n")
