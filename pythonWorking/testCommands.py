
#cd "C:\Users\jaese\Desktop\programming folder\python\pythonWorking\tests"

import unittest
import main
import commands

class TestStringMethods(unittest.TestCase):

    def test_valid_date_format(self):
        result = main.dateCheck("date", ["main.py", "date", "2026-07-20"])
        self.assertEqual(result, "2026-07-20")

    def test_valid_separator(self):
        result = main.dateCheck ("date", ["main.py", "date", "2026/07/20"])
        self.assertIsNone(result)


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

