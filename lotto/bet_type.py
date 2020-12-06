class BetType:
    """Represents a type of bet of a ticket.

    Attributes:
        __bet_type: int     is a index for bet_type_allowed list
    """
    # bet_types = {'Ambata': 1, 'Ambo': 2, 'Terno': 3, 'Quaterna': 4, 'Cinquina': 5}
    bet_type_allowed = ['Ambata', 'Ambo', 'Terno', 'Quaterna', 'Cinquina']

    def __init__(self, bet_type=0):
        self.__bet_type = bet_type  # bet_type:
        self.min_amount_numbers = bet_type + 1

    def get(self):
        return self.__bet_type

    def get_name(self):
        return BetType.bet_type_allowed[self.__bet_type]

    @staticmethod
    def get_max_index():
        return len(BetType.bet_type_allowed) - 1

    @staticmethod
    def get_min_index():
        return 0


def test():
    for i in range(len(BetType.bet_type_allowed)):
        bet_type_01 = BetType(i)
        name = bet_type_01.get_name()
        print(name)


if __name__ == '__main__':
    test()
