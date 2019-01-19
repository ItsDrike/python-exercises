import unittest
import Solution


class TestSolution(unittest.TestCase):
    """Test for Solution"""

    def test_main(self):
        result = Solution.main()
        self.assertEqual(result, """2, 8, 34, 144, 610, 2584, 10946""")


if __name__ == '__main__':
    unittest.main()
