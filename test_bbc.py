import unittest
from unittest.mock import patch
from bbc import main
from os import remove
import sys
import io


TMP_FILE = "test.out.bib"


class TestStringMethods(unittest.TestCase):
    def test_parse_args(self):
        testargs = ["bbc", "--input", "test.bib", "--output", TMP_FILE]
        with patch.object(sys, "argv", testargs):
            main()

        with open(TMP_FILE) as result, open("test_result.bib") as expected:
            self.assertListEqual(list(result), list(expected))

    def tearDown(self):
        remove(TMP_FILE)


if __name__ == "__main__":
    unittest.main()
