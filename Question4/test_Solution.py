import unittest
import Solution


class TestSolution(unittest.TestCase):
    """Test for Solution"""

    def test_main_1(self):
        result = Solution.main('ABCDEFGHIJKLMNOPQRSTUV')
        self.assertEqual(result, """EFGHIJKLMNOPQRSTUVWXYZ""")

    def test_main_2(self):
        result = Solution.main('WXYZ')
        self.assertEqual(result, """ABCD""")

    def test_main_3(self):
        result = Solution.main('1 5 8 + * abcde fghi jklm nopq rstuv wxyz')
        self.assertEqual(result, """1 5 8 + * efghi jklm nopq rstu vwxyz abcd""")

    def test_main_4(self):
        result = Solution.main(Solution.main("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce viverra id tellus non bibendum. Suspendisse rhoncus eu libero eget porta. Integer et sodales velit, vitae venenatis lectus. Vestibulum ac gravida nisi. Praesent lectus magna, porttitor at euismod in, pulvinar vel tortor. Etiam nec dolor vestibulum, commodo metus ut, placerat lectus. Duis fringilla venenatis ante eget maximus. Nam tellus velit, iaculis vitae sem et, aliquam sagittis ligula. Sed egestas id sem porttitor imperdiet. Curabitur sem sapien, mollis vel posuere sit amet, hendrerit sit amet nisi. Etiam at massa a est pulvinar imperdiet sit amet sed erat."""))
        self.assertEqual(result, """Twzmu qxacu lwtwz aqb iumb, kwvamkbmbcz ilqxqakqvo mtqb. Ncakm dqdmzzi ql bmttca vwv jqjmvlcu. Acaxmvlqaam zpwvkca mc tqjmzw momb xwzbi. Qvbmomz mb awlitma dmtqb, dqbim dmvmvibqa tmkbca. Dmabqjctcu ik ozidqli vqaq. Xzimamvb tmkbca uiovi, xwzbbqbwz ib mcqauwl qv, xctdqviz dmt bwzbwz. Mbqiu vmk lwtwz dmabqjctcu, kwuuwlw umbca cb, xtikmzib tmkbca. Lcqa nzqvoqtti dmvmvibqa ivbm momb uifquca. Viu bmttca dmtqb, qikctqa dqbim amu mb, itqyciu aioqbbqa tqocti. Aml momabia ql amu xwzbbqbwz quxmzlqmb. Kczijqbcz amu aixqmv, uwttqa dmt xwacmzm aqb iumb, pmvlzmzqb aqb iumb vqaq. Mbqiu ib uiaai i mab xctdqviz quxmzlqmb aqb iumb aml mzib.""")


if __name__ == '__main__':
    unittest.main()
