class Yatzy:

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def chance(*dice):
        # While, mientras haya dados, que vaya sumando sus valores
        total = 0
        for d in dice:
            total += d
        return total

    @staticmethod
    def yatzy(dice):
        if dice.count(dice[0]) == 5:
            return 50
        return 0

    @staticmethod
    def ones(*dice):
        sum = 0
        for d in dice:
            if (d == 1):
                sum += 1
        return sum

    @staticmethod
    def twos(*dice):
        sum = 0
        for d in dice:
            if (d == 2):
                sum += 2
        return sum

    @staticmethod
    def threes(*dice):
        sum = 0
        for d in dice:
            if (d == 3):
                sum += 3
        return sum

    @staticmethod
    def fours(*dice):
        sum = 0
        for d in dice:
            if (d == 4):
                sum += 4
        return sum

    @staticmethod
    def fives(*dice):
        sum = 0
        for d in dice:
            if (d == 5):
                sum += 5
        return sum

    @staticmethod
    def sixes(*dice):
        sum = 0
        for d in dice:
            if (d == 6):
                sum += 6
        return sum

    @staticmethod
    def one_pair(*dice):
        num = []
        for d in dice:
            if dice.count(d) == 2:
                num.append(d)
        return max(set(num)) * 2

    @staticmethod
    def two_pair(*dice):
        num = []
        for d in dice:
            if dice.count(d) >= 2:
                num.append(d)
        if len(set(num)) > 1:
            return sum(set(num)) * 2
        else:
            return 0

    @staticmethod
    def three_of_a_kind(*dice):
        num = []
        for d in dice:
            if dice.count(d) >= 3:
                num.append(d)
            return sum(set(num)) * 3

    @staticmethod
    def four_of_a_kind(*dice):
        num = []
        for d in dice:
            if dice.count(d) >= 4:
                num.append(d)
            return sum(set(num)) * 4

    @staticmethod
    def smallStraight(*dice):
        num = []
        i = 1
        for d in range(0, len(dice) + 1):
            if i in dice and i <= 5:
                num.append(i)
                i = i + 1
            elif len(num) < 5:
                return 0
        return sum(num)

    @staticmethod
    def largeStraight(*dice):
        num = []
        i = 2
        for d in range(0, len(dice) + 1):
            if i in dice and i <= 6:
                num.append(i)
                i = i + 1
            elif len(num) < 5:
                return 0
        return sum(num)

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
