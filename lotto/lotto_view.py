from ticket import Ticket
from city import City
from bet_type import BetType


class LottoView:
    @staticmethod
    def show_ticket(ticket_, index_=None):
        """Print all attributes of a ticket"""
        city_ = ticket_.city.get_name()
        bet_type = ticket_.bet_type.get_name()
        numbers = ticket_.numbers
        if index_ is not None:
            print("--- Ticket n°{} ---".format(index_))
        else:
            print("--- Ticket ---".format(index_))
        print("- City :")
        print("{}".format(city_))
        print("- Bet Type :")
        print("{}".format(bet_type))
        print("- Numbers :")
        for n in numbers:
            print(n, end=" ")
        print()


if __name__ == '__main__':

    city = City(1)
    bet_type = BetType(1)
    amount_of_numbers = 10
    t = Ticket(city=city, bet_type=BetType(4), amount_of_numbers=10)
    LottoView.show_ticket(t)
