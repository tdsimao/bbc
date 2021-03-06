import unittest
from unittest.mock import patch
from bbc import main
from os import remove
from os import path
import sys
from io import StringIO
from contextlib import redirect_stderr


INPUT_FILE = "tests/data/test.bib"
TMP_FILE = "test.out.bib"


class IntegrationTest(unittest.TestCase):
    def test_add_todo(self):
        testargs = ["bbc", INPUT_FILE, "--output", TMP_FILE, "--add-todo"]
        with patch.object(sys, "argv", testargs):
            with redirect_stderr(StringIO()):
                main()

        with open(TMP_FILE) as result, open("tests/data/test_result.bib") as expected:
            self.assertListEqual(list(result), list(expected))

    def test_no_todo(self):
        testargs = ["bbc", INPUT_FILE, "--output", TMP_FILE]
        with patch.object(sys, "argv", testargs):
            with redirect_stderr(StringIO()):
                main()
        with open(TMP_FILE) as result, open("tests/data/test_result_no_todo.bib") as expected:
            self.assertListEqual(list(result), list(expected))


    def tearDown(self):
        if path.exists(TMP_FILE):
            remove(TMP_FILE)


if __name__ == "__main__":
    unittest.main()
