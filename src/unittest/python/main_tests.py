# all test files should end with file name "_tests.py"
from mockito import mock, verify
import unittest

from main import main_handler


class HelloWorldTest(unittest.TestCase):
    # all test methods should start with name "test_", else it will be ignored
    @staticmethod
    def test_main_should_issue_hello_world_message():
        out = mock()

        main_handler(out)

        verify(out).write("Hello world from python module\n")
