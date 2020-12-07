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
        ticket_id: int
        # cost: double (not in Learning Path level 1)
    """

    def __init__(self, city=City(), bet_type=BetType(), amount_of_numbers=10, numbers=None, ticket_id=1):
        """
        Ticket constructor.
        If the *numbers* argument is not provided, *amount_of_numbers* distinct random numbers are generated.

        Args:
            city:
            bet_type:
            amount_of_numbers:
            numbers:
            ticket_id:
        """
        if numbers is None:
            self.numbers = self.generate_numbers(amount_of_numbers)
        else:
            if self.check_numbers(numbers):
                self.numbers = numbers
            else:
                raise Exception("Sorry, wrong numbers argument")
        self.city = city
        self.bet_type = bet_type
        self.id = ticket_id

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

    @staticmethod
    def check_numbers(numbers):
        numbers_are_valid = 1 <= len(numbers) <= 10
        if not numbers_are_valid:
            print("The amount of numbers is {:d} and it's out of range [1..10]".format(len(numbers)))
        else:
            numbers_are_valid = all(1 <= num <= 90 for num in numbers)
            if not numbers_are_valid:
                print("Each number must be between 1 and 90")
            else:
                numbers.sort()
                for i in range(len(numbers) - 1):
                    duplicated_numbers = numbers[i] == numbers[i + 1]
                    numbers_are_valid = numbers_are_valid and not duplicated_numbers
                    if duplicated_numbers:
                        print("duplicated numbers: ", numbers[i], numbers[i + 1])
        return numbers_are_valid


if __name__ == '__main__':
    # make a ticket
    city_01 = City(0)
    bet_type_01 = BetType(1)
    ticket_01 = Ticket(city=city_01, bet_type=bet_type_01, amount_of_numbers=10)
    print(ticket_01.numbers)
    # assert ticket.validate()

    ticket_02 = Ticket(city=city_01, amount_of_numbers=10)
    print(ticket_02.numbers)
    # assert not ticket_02.validate()

    ticket_03 = Ticket(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 90])
    print(ticket_03.numbers)

    """ticket_04 = Ticket(4, 0, 10)
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
