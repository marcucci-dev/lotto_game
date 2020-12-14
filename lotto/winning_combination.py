from itertools import combinations

prize_for_one = {1: [11.23],
                 2: [ 5.62, 250.00],
                 3: [ 3.74,  83.33, 4500.00],
                 4: [ 2.81,  41.67, 1125.00, 120000.00],
                 5: [ 2.25,  25.00,  450.00,  24000.00, 6000000.00],
                 6: [ 1.87,  16.67,  225.00,   8000.00, 1000000.00],
                 7: [ 1.60,  11.90,  128.57,   3428.57,  285714.29],
                 8: [ 1.40,   8.93,   80.36,   1714.29,  107142.86],
                 9: [ 1.25,   6.94,   53.57,    952.38,   47619.05],
                 10:[ 1.12,   5.56,   37.50,    571.43,   23809.52]}


class WinningCombination:
    def __init__(self, city, bet_type, winning_numbers, amount_winning_combinations, amount_numbers_played, prize,
                 ticket_id):
        """

        Args:
            ticket_id
            city
            bet_type
            winning_numbers (object):
        """
        self.ticket_id = ticket_id
        self.city = city
        self.bet_type = bet_type
        self.winning_numbers = winning_numbers
        # self.amount_winning_combinations = len(list(combinations(winning_numbers, bet_type.min_amount_numbers)))
        self.amount_winning_combinations = amount_winning_combinations
        self.amount_numbers_played = amount_numbers_played

        # self.prize = prize_for_one[self.amount_numbers_played][self.bet_type.get()] * self.amount_winning_combinations
        self.prize = prize


class Winner:
    def __init__(self, winning_combinations, total_prize, gross_prize, ticket_id):
        """
        Args:
            ticket_id
            total_prize
            gross_prize
            winning_combinations List[WinningCombination]:
        """
        self.ticket_id = ticket_id
        self.total_prize = total_prize
        self.gross_prize = gross_prize
        self.winning_combinations = winning_combinations
