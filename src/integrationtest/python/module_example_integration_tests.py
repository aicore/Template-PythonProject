import requests
import unittest


class Test(unittest.TestCase):
    """Class contain different integration test cases"""

    # noinspection PyMethodMayBeStatic
    @staticmethod
    def test_sample():
        """Makes an http call and checks the status code"""
        response = requests.get("https://www.google.com/")
        if response.status_code != 200:
            raise AssertionError


if __name__ == "__main__":
    unittest.main()
