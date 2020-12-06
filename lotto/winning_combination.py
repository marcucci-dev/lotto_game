from itertools import combinations


class WinningCombination:
    def __init__(self, city, bet_type, winning_numbers, ticket_id):
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
        self.amount_winning_combinations = len(list(combinations(winning_numbers, bet_type.min_amount_numbers)))
