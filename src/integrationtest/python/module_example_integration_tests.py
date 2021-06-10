import http.client
import unittest


class Test(unittest.TestCase):

    """Class contain different integrtion test cases"""

    # noinspection PyMethodMayBeStatic
    @staticmethod
    def test_sample():
        """Makes an http call and checks the status code"""
        conn = http.client.HTTPSConnection("www.google.com")
        conn.request("GET", "/")
        response = conn.getresponse()
        if response.status != 200:
            raise AssertionError


if __name__ == "__main__":
    unittest.main()
