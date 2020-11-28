class BetType:
    bet_types = {'Ambata': 1, 'Ambo': 2, 'Terno': 3, 'Quaterna': 4, 'Cinquina': 5}

    def __init__(self, bet_type):
        self.bet_type = bet_type  # bet_type:

    def get_name(self):
        for i in BetType.bet_types:
            if BetType.bet_types[i] == self.bet_type:
                return i


def test():
    bet_type_01 = BetType(1)
    name = bet_type_01.get_name()
    print(name)


if __name__ == '__main__':
    test()
