import Solution4 as Solution


def test_main_none():
    x, y = Solution.main(['STOP'])
    assert x == 0
    assert y == 0


def test_main_set():
    x, y = Solution.main(['FORWARD 0', 'STOP'])
    assert x == 0
    assert y == 0
    x, y = Solution.main(['FORWARD 8', 'STOP'])
    assert x == 0
    assert y == 8
    x, y = Solution.main(['RIGHT 8', 'STOP'])
    assert x == 8
    assert y == 0
    x, y = Solution.main(['FORWARD 8', 'RIGHT 8', 'STOP'])
    assert x == 8
    assert y == 8
    x, y = Solution.main(['BACKWARD 8', 'LEFT 8', 'STOP'])
    assert x == -8
    assert y == -8
    x, y = Solution.main(['FORWARD -8', 'RIGHT -8', 'STOP'])
    assert x == -8
    assert y == -8


def test_main_add():
    x, y = Solution.main(['FORWARD 8', 'FORWARD 8', 'STOP'])
    assert x == 0
    assert y == 16
    x, y = Solution.main(['BACKWARD 8', 'BACKWARD 8', 'STOP'])
    assert x == 0
    assert y == -16
    x, y = Solution.main(['RIGHT 8', 'RIGHT 8', 'STOP'])
    assert x == 16
    assert y == 0
    x, y = Solution.main(['LEFT 8', 'LEFT 8', 'STOP'])
    assert x == -16
    assert y == 0
    x, y = Solution.main(['FORWARD 0', 'FORWARD 8', 'BACKWARD -8', 'RIGHT 10', 'RIGHT 15', 'LEFT 5', 'STOP'])
    assert x == 20
    assert y == 16
