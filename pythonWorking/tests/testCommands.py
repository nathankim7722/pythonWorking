
#cd "C:\Users\jaese\Desktop\programming folder\python\pythonWorking\tests"
#python -m unittest tests.test_commands -v

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import main
import commands
from storage import loadEntries, saveEntries, appendEntries, saveJson


class TestStringMethods(unittest.TestCase):

    def test_valid_same_date(self):
        entries = [
            {
                "date":"2026-07-20",
                "text":"python 공부"
            },
            {
                "date":"2026-07-22",
                "text":"GitHub"
            }
        ]
        result = main.has_entry(entries, "2026-07-22")
        self.assertTrue(result)


    def test_valid_date_format(self):
        result = main.dateCheck("date", ["main.py", "date", "2026-07-20"])
        self.assertEqual(result, "2026-07-20")


    def test_valid_separator(self):
        result = main.dateCheck ("date", ["main.py", "date", "2026/07/20"])
        self.assertIsNone(result)


    def test_valid_date_calander(self):
        result = main.dateCheck ("date", ["main.py", "date", "2020-02-29"])
        self.assertEqual(result, "2020-02-29")


    def test_search_query(self):

        entries = [
            {
                "date":"2026-07-20",
                "text":"python 공부"
            },
            {
                "date":"2026-07-21",
                "text":"GitHub"
            }
        ]

        result = commands.search(entries,"python")

        self.assertEqual(len(result),1)


if __name__ == '__main__':
    unittest.main()

