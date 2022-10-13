import unittest
import json
import requests


def validate_json(url):
    r = requests.get(url)
    try:
        json.loads(r.text)
        print("Json syntax is valid")
        return True
    except ValueError as err:
        print(err)
        return False


class Test_API(unittest.TestCase):

    def setUp(self):
        self.api_url = "https://cepdnaclk.github.io/undergraduate-courses/api/courses/"

    def test_api_json_syntax(self):
        self.assertTrue(validate_json(self.api_url),"Json syntax in API is invalid")


if __name__ == '__main__':
    unittest.main()