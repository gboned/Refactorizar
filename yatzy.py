class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        total = 0
        for die in dice:
            total += die
        return total

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == 5:
            return 50
        return 0

    @staticmethod
    def ones(*dice):
        sum = 0
        for die in dice:
            if die == 1:
                sum += 1
        return sum

    @staticmethod
    def twos(*dice):
        sum = 0
        for die in dice:
            if die == 2:
                sum += 2
        return sum

    @staticmethod
    def threes(*dice):
        sum = 0
        for die in dice:
            if die == 3:
                sum += 3
        return sum

    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX

    @staticmethod
    def one_pair(*dice):
        num = []
        for die in dice:
            if dice.count(die) == 2:
                num.append(die)
        return max(set(num)) * 2

    @staticmethod
    def two_pair(*dice):
        num = []
        for die in dice:
            if dice.count(die) >= 2:
                num.append(die)
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
    def fullHouse(*dice):
        num = []
        for d in dice:
            if dice.count(d) in (2, 3):
                num.append(d)
        return sum(num)
