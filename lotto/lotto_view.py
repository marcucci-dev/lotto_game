from ticket import Ticket
from city import City
from bet_type import BetType
from extraction import Extraction
from winning_combination import WinningCombination


class LottoView:
    @staticmethod
    def show_ticket(ticket_, index_=None):
        """Print all attributes of a ticket"""
        '''if ticket_.city.all_cities:
            city_ = 'Tutte'
        else:
            city_ = ticket_.city.get_name()'''
        city_ = 'Tutte' if ticket_.city.all_cities else ticket_.city.get_name()
        bet_type_ = ticket_.bet_type.get_name()
        numbers = ticket_.numbers
        if index_ is not None:
            print("--- Ticket n°{} ---".format(index_))
        else:
            print("--- Ticket ---".format(index_))

        width_ = 1
        # print("{:>10} : {:{w}} ".format("City", city_, w=width_))
        print("{:>10} : {} ".format("City", city_, w=width_))
        print("{:>10} : {:{w}} ".format("Bet type", bet_type_, w=width_))
        print("{:>10} :".format("Numbers", d=numbers, w=width_), end=" ")
        for n in numbers:
            print(n, end=" ")
        print()
        print()

    @staticmethod
    def show_extraction(extraction):
        """Print values of an extraction"""
        print("--- Extraction ---")
        # print(extraction.drawn_numbers)
        for c in Extraction.city_list:
            # print("{:>10} {}".format(c, extraction.drawn_numbers[c]))
            print("{:>10} {d[0]:>{w}} {d[1]:>{w}} {d[2]:>{w}} {d[3]:>{w}} {d[4]:>{w}}"
                  .format(c, d=extraction.drawn_numbers[c], w=3))

    @staticmethod
    def show_winners(winning_combination):
        """Print values of an winning combination"""
        wc = winning_combination
        # print(winning_combination.ticket_id)
        print("city", wc.city)
        print("\t", wc.amount_winning_combinations, wc.bet_type.get_name(),
              "with", wc.winning_numbers, "on", wc.amount_numbers_played, "numbers played")


if __name__ == '__main__':

    city = City(all_cities=False, city=1)
    # city = City(True)
    bet_type = BetType(4)
    amount_of_numbers = 10
    t = Ticket(city=city, bet_type=BetType(4), amount_of_numbers=10)
    LottoView.show_ticket(t)

    LottoView.show_extraction(Extraction())

    print()
    winning_numbers = [1, 2, 3, 4, 5]
    amount_numbers_played = 10
    ticket_id = 5
    LottoView.show_winners(WinningCombination(city, bet_type, winning_numbers, amount_numbers_played, ticket_id))
