import Solution3 as Solution


def test_main_set():
    result = Solution.main('ABCDEFGHIJKLMNOPQRSTUV')
    assert result == 'EFGHIJKLMNOPQRSTUVWXYZ'


def test_main_overflow():
    result = Solution.main('WXYZ')
    assert result == 'ABCD'


def test_main_special_chars():
    result = Solution.main('1 5 8 + * abcde fghi jklm nopq rstuv wxyz')
    assert result == '1 5 8 + * efghi jklm nopq rstu vwxyz abcd'


def test_main_long_text():
    result = Solution.main(Solution.main("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce viverra id tellus non bibendum. Suspendisse rhoncus eu libero eget porta. Integer et sodales velit, vitae venenatis lectus. Vestibulum ac gravida nisi. Praesent lectus magna, porttitor at euismod in, pulvinar vel tortor. Etiam nec dolor vestibulum, commodo metus ut, placerat lectus. Duis fringilla venenatis ante eget maximus. Nam tellus velit, iaculis vitae sem et, aliquam sagittis ligula. Sed egestas id sem porttitor imperdiet. Curabitur sem sapien, mollis vel posuere sit amet, hendrerit sit amet nisi. Etiam at massa a est pulvinar imperdiet sit amet sed erat.2*"""))
    assert result == """Twzmu qxacu lwtwz aqb iumb, kwvamkbmbcz ilqxqakqvo mtqb. Ncakm dqdmzzi ql bmttca vwv jqjmvlcu. Acaxmvlqaam zpwvkca mc tqjmzw momb xwzbi. Qvbmomz mb awlitma dmtqb, dqbim dmvmvibqa tmkbca. Dmabqjctcu ik ozidqli vqaq. Xzimamvb tmkbca uiovi, xwzbbqbwz ib mcqauwl qv, xctdqviz dmt bwzbwz. Mbqiu vmk lwtwz dmabqjctcu, kwuuwlw umbca cb, xtikmzib tmkbca. Lcqa nzqvoqtti dmvmvibqa ivbm momb uifquca. Viu bmttca dmtqb, qikctqa dqbim amu mb, itqyciu aioqbbqa tqocti. Aml momabia ql amu xwzbbqbwz quxmzlqmb. Kczijqbcz amu aixqmv, uwttqa dmt xwacmzm aqb iumb, pmvlzmzqb aqb iumb vqaq. Mbqiu ib uiaai i mab xctdqviz quxmzlqmb aqb iumb aml mzib.2*"""
