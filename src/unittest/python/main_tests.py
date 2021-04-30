# all test files should end with file name "_tests.py"
from mockito import mock, verify
import unittest

from main import main_handler
import test_utils


class HelloWorldTest(unittest.TestCase):
    # all test methods should start with name "test_", else it will be ignored
    # all tests should have the below noinspection static clause to prevent
    # test case may be static pylint errors with py tests.
    # noinspection PyMethodMayBeStatic
    def test_main_should_issue_hello_world_message(self):
        out = mock()

        main_handler(out)

        verify(out).write("Hello world from python module\n")

    # noinspection PyMethodMayBeStatic
    def test_should_load_json_test_resource(self):
        json_test_resource_file_name = 'json_sample.json'
        json_data = test_utils.load_json_test_resource(json_test_resource_file_name)
        assert json_data['message'] == 'hello world'
