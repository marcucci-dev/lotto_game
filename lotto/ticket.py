import os
import sys

# print(sys.path)

import random

# from lotto.table import Table  # GOOD from PyCharm, but BAD from terminal!!!

# Single module: GOOD from PyCharm & from terminal, but alert "Unresolved reference 'Table'" in PyCharm!!!
# from lotto_game.py: BAD
# from table import Table
from city import City
from bet_type import BetType


class Ticket:
    """Represents a ticket of the lotto game.
    ...
    Attributes
    ----------
        city: City object
        bet_type: BetType object
        numbers: list of int
        # cost: double (not in Learning Path level 1)
    """

    def __init__(self, city=City(0), bet_type=BetType(0), amount_of_numbers=10):
        self.numbers = self.generate_numbers(amount_of_numbers)
        if self.check_numbers():
            self.city = city
            self.bet_type = bet_type

        else:
            raise Exception("Sorry, Ticket.__init__ raise an exception")

    # def __str__(self):
    #    """Returns a human-readable string representation."""
    #    """return '{bet_type} of {amount_of_numbers} numbers on {city} ruota: ' \
    #           '\n\t{numbers}'.format(bet_type=Ticket.type_names[self.bet_type], city=Ticket.city_names[self.city],
    #                                  numbers=self.numbers, amount_of_numbers=len(self.numbers))
    #    """
    #    return self.table_layout.__str__()

    @staticmethod
    def generate_numbers(amount_of_numbers):
        # create a list of integers from 1 to 90 from which the numbers will be extracted
        numbers_to_extract = [j + 1 for j in range(90)]
        numbers_drawn_list = []
        for i in range(amount_of_numbers):
            index_drawn = random.randint(0, 89 - i)
            number_drawn = numbers_to_extract[index_drawn]
            numbers_drawn_list.append(number_drawn)
            del numbers_to_extract[index_drawn]
        return numbers_drawn_list

    def check_numbers(self):
        numbers_are_valid = 1 <= len(self.numbers) <= 10
        if not numbers_are_valid:
            print("The amount of numbers = {:d} is out of range [1..10]".format(len(self.numbers)))
        else:
            self.numbers.sort()
            for i in range(len(self.numbers) - 1):
                duplicated_numbers = self.numbers[i] == self.numbers[i + 1]
                numbers_are_valid = numbers_are_valid and not duplicated_numbers
                if duplicated_numbers:
                    print("duplicated numbers: ", self.numbers[i], self.numbers[i + 1])
        return numbers_are_valid


if __name__ == '__main__':
    # make a ticket
    city_01 = City(0)
    bet_type_01 = BetType(1)
    ticket_01 = Ticket(city=city_01, bet_type=bet_type_01, amount_of_numbers=10)
    print(ticket_01)
    # assert ticket.validate()

    ticket_02 = Ticket(city=city_01, amount_of_numbers=10)
    print(ticket_02)
    # assert not ticket_02.validate()
    """
    ticket_03 = Ticket(4, 1, 11)
    assert not ticket_03.validate()

    ticket_04 = Ticket(4, 0, 10)
    assert not ticket_04.validate()

    ticket_05 = Ticket(4, 11, 10)
    assert not ticket_05.validate()

    ticket_06 = Ticket()
    ticket_06.numbers = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]
    assert not ticket_06.validate()

    ticket_07 = Ticket()
    ticket_07.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 90, 90]
    assert not ticket_07.validate()
    """
