import os
import sys

# print(sys.path)
# print("-------------------------------------")
# del sys.path[0]
# sys.path.append((os.path.dirname(os.path.realpath(__file__)) ))
# sys.path.append((os.path.dirname(os.path.realpath(__file__)) , '..'))  # GOOD
# sys.path.append('C:\\Users\\giuseppe\\PycharmProjects\\lotto_game_Level_01\\lotto_game\\lotto\\')
print(sys.path)

import random

# from lotto.table import Table  # GOOD from PyCharm, but BAD from terminal!!!

# Single module: GOOD from PyCharm & from terminal, but alert "Unresolved reference 'Table'" in PyCharm!!!
# from lotto_game.py: BAD
from table import Table
# from . import Table
from city import City
from bet_type import BetType


class Ticket:
    """Represents a ticket of the lotto game.

    Attributes:
        city: integer 0-10
        bet_type: integer 0-4
        numbers: list of int
        # cost: double (not in Learning Path level 1)

        table_layout: object to print the generated tickets with nice ascii art table decoration.
    """

    # type_names = ["ambata", "ambo", "terno", "quaterna", "cinquina"]
    # city_names = ["Tutte", "Bari", "Cagliari", "Firenze", "Genova",
    #              "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

    def __init__(self, city=City(0), bet_type=BetType(1), amount_of_numbers=10):
        self.numbers = self.generate_numbers(amount_of_numbers)
        if self.check_numbers():
            self.city = city
            self.bet_type = bet_type
            self.table_layout = Table()
            self.table_layout.set_fields_names(["Numbers", "Ruota", "Type"])
            # if self.check_type() and self.check_numbers() and self.check_city():
            self.table_layout.set_fields_values((self.list_number_to_str(), City.city_allowed[self.city.get()],
                                                 self.bet_type.get_name()))
        else:
            raise Exception("Sorry, Ticket.__init__ raise an exception")

        self.table_layout.set_fields_widths()

    def __str__(self):
        """Returns a human-readable string representation."""
        """return '{bet_type} of {amount_of_numbers} numbers on {city} ruota: ' \
               '\n\t{numbers}'.format(bet_type=Ticket.type_names[self.bet_type], city=Ticket.city_names[self.city],
                                      numbers=self.numbers, amount_of_numbers=len(self.numbers))
        """
        return self.table_layout.__str__()

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

    '''def check_type(self):
        is_valid = 0 <= self.bet_type < len(self.type_names)
        if not is_valid:
            print("The self.bet_type = {:d} is out of range [0..{:d}]".format(self.bet_type, len(self.type_names) - 1))
        return is_valid
    '''
    '''def check_city(self):
        is_valid = 0 <= self.city < len(self.city_names)
        if not is_valid:
            print("The self.city = {:d} is out of range [0..{:d}]".format(self.city, len(self.city_names) - 1))
        return is_valid
    '''

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

    def validate(self):
        # type_is_valid = self.check_type()
        # city_is_valid = self.check_city()
        numbers_are_valid = self.check_numbers()
        return numbers_are_valid and city_is_valid  # and type_is_valid

    def list_number_to_str(self):
        out = ""
        for num in self.numbers:
            out += str(num) + " "
        return out


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
