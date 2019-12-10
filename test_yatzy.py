from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance():
    assert Yatzy.chance(2, 3, 4, 5, 1) == 15
    assert Yatzy.chance(3, 3, 4, 5, 1) == 16


def test_yatzy():
    assert Yatzy.yatzy(6, 6, 6, 6, 6) == 50
    assert Yatzy.yatzy(6, 6, 6, 6, 3) == 0


def test_ones():
    assert Yatzy.ones(1, 2, 3, 4, 5) == 1
    assert Yatzy.ones(1, 2, 1, 4, 5) == 2
    assert Yatzy.ones(6, 2, 2, 4, 5) == 0
    assert Yatzy.ones(1, 2, 1, 1, 1) == 4


def test_twos():
    assert Yatzy.twos(1, 2, 3, 2, 6) == 4
    assert Yatzy.twos(2, 2, 2, 2, 2) == 10


def test_threes():
    assert Yatzy.threes(1, 2, 3, 2, 3) == 6
    assert Yatzy.threes(2, 3, 3, 3, 3) == 12


def test_fours():
    assert Yatzy(4, 4, 4, 5, 5).fours() == 12
    assert Yatzy(4, 4, 5, 5, 5).fours() == 8
    assert Yatzy(4, 5, 5, 5, 5).fours() == 4


def test_fives():
    assert Yatzy(4, 4, 4, 5, 5).fives() == 10
    assert Yatzy(4, 4, 5, 5, 5).fives() == 15
    assert Yatzy(4, 5, 5, 5, 5).fives() == 20


def test_sixes():
    assert Yatzy(4, 4, 4, 5, 5).sixes() == 0
    assert Yatzy(4, 4, 6, 5, 5).sixes() == 6
    assert Yatzy(6, 5, 6, 6, 5).sixes() == 18


def test_one_pair():
    assert Yatzy.one_pair(3, 4, 3, 5, 6) == 6
    assert Yatzy.one_pair(5, 3, 3, 3, 5) == 10
    assert Yatzy.one_pair(5, 3, 6, 6, 5) == 12


def test_two_pair():
    assert Yatzy.two_pair(3, 3, 5, 4, 5) == 16
    assert Yatzy.two_pair(3, 3, 6, 6, 6) == 18
    assert Yatzy.two_pair(3, 3, 6, 5, 4) == 0


def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)


def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
