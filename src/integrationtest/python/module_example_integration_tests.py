import urllib.request
import unittest


class Test(unittest.TestCase):
    """Class contain different integrtion test cases"""

    # noinspection PyMethodMayBeStatic
    @staticmethod
    def test_sample():
        """Makes an http call and checks the status code"""
        weburl = urllib.request.Request('https://www.google.com/')
        with urllib.request.urlopen(weburl) as response:
            code = response.getcode()
        if code != 200:
            raise AssertionError


if __name__ == "__main__":
    unittest.main()
