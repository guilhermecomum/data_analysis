import unittest
from data_analysis import test_func

class TestDataAnalysis(unittest.TestCase):
    def test_read_file(self):

        self.assertEqual(test_func(), True)


if __name__ == '__main__':
    unittest.main()
