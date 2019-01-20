import Solution7s as Solution
import json


def main(string):
    characters = list(string)
    counted_chars = {}
    char_count = 0

    for char in characters:
        if char != ' ':
            counted_chars[char] = characters.count(char)
            char_count += 1

    for key in counted_chars:
        percentual_appearance = (counted_chars[key] / char_count) * 100
        counted_chars[key] = round(percentual_appearance, 2)
    return json.dumps(counted_chars, indent=4)


def test_main_set():
    result = set(repr(x) for x in Solution.main('abcdefghijklmnopqrstuvwxyz'))
    assert result == set(repr(x) for x in main('abcdefghijklmnopqrstuvwxyz'))
    result = set(repr(x) for x in Solution.main('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    assert result == set(repr(x) for x in main('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


def test_main_upper_lower():
    result = set(repr(x) for x in Solution.main('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
    assert result == set(repr(x) for x in main('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))


def test_main_duplicates():
    result = set(repr(x) for x in Solution.main('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    assert result == set(repr(x) for x in main('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    result = set(repr(x) for x in Solution.main('aaA'))
    assert result == set(repr(x) for x in main('aaA'))
    result = set(repr(x) for x in Solution.main('aaaaBa'))
    assert result == set(repr(x) for x in main('aaaaBa'))


def test_main_special_chars():
    result = set(repr(x) for x in Solution.main('*/-++'))
    assert result == set(repr(x) for x in main('*/-++'))
