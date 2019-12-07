class Yatzy:

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
    def fullHouse(*dice):
        num = []
        for d in dice:
            if dice.count(d) in (2, 3):
                num.append(d)
        return sum(num)
