from city import City
from bet_type import BetType
from ticket import Ticket
from extraction import Extraction
from winning_combination import WinningCombination, Winner
from lotto_view import LottoView


class LottoController:
    @staticmethod
    def check_input(prompt, min_value, max_value, range_=None, is_float=False):
        """Read a string from standard input until an integer value is provided
        within the bounds min_value and max_value.
        The prompt string is printed to standard output before reading input.
        Returns an integer entered by the user between min_value and max_value.

        Args:
            prompt: string
            min_value :  int
            max_value:   int
            range_:
            is_float: bool

        Returns:
            user_input: int
        """
        while True:
            user_input = input(prompt)

            if is_float:
                try:
                    user_input = float(user_input)
                except ValueError:
                    print("Input type must be float\n")
                    continue
            else:
                try:
                    user_input = int(user_input)
                except ValueError:
                    print("Input type must be int\n")
                    continue

            # if user_input not in range_:
            #    print("Input must be in range [{0.start}..{0.stop}).\n".format(range_))
            # print("min e max", min_value, max_value)
            if user_input < min_value:
                print("Input must be greater than or equal to {0}.\n".format(min_value))
            elif user_input > max_value:
                print("Input must be less than or equal to {0}.\n".format(max_value))
            elif user_input % 0.5 != 0:
                print("Input must be multiple of {0}.\n".format(0.5))
            else:
                return user_input

    @staticmethod
    def select_num_of_tickets():
        prompt = "How many tickets do you want to generate (min: 1, max: 5, exit: 0) \n"
        # range_ = range(10)
        return LottoController.check_input(prompt, min_value=0, max_value=5)

    @staticmethod
    def select_city():
        suffix = "\n\t0: Tutte "
        for j in range(City.get_max_index() + 1):
            suffix += "\n\t" + str(j + 1) + ": " + City.city_allowed[j] + " "
        prompt = "Choose the \"city\" (aka \"ruota\"): " + suffix + "\n"
        all_cities_value = 0
        city_index = LottoController.check_input(prompt, min_value=all_cities_value, max_value=City.get_max_index() + 1)
        all_cities = city_index == 0
        a_city = City(all_cities=all_cities, city=city_index - 1)
        return a_city

    @staticmethod
    def select_bet_type():
        suffix = ""
        for j in range(BetType.get_max_index() + 1):
            suffix += "\n\t" + str(j + 1) + ": " + str(BetType.bet_type_allowed[j]) + " "
        prompt = "Choose the type of bet:" + suffix + "\n"
        bet_type = LottoController.check_input(prompt, min_value=BetType.get_min_index() + 1,
                                               max_value=BetType.get_max_index() + 1)
        a_bet_type = BetType(bet_type - 1)
        return a_bet_type

    @staticmethod
    def select_amount_of_numbers(bet_type):
        min_for_bet_type = bet_type.get() + 1
        max_for_bet_type = 10
        prompt = "Choose the amount of numbers to generate (min {} max {} per this bet): \n".format(min_for_bet_type,
                                                                                                   max_for_bet_type)
        return LottoController.check_input(prompt, min_value=min_for_bet_type, max_value=10)

    @staticmethod
    def select_cost():
        prompt = "Choose the cost of bet (min €{} max €{} per bet): \n".format(1.0, 200.0)
        cost = LottoController.check_input(prompt, min_value=1.0, max_value=200.0, is_float=True)
        return cost

    @staticmethod
    def insert_ticket(ticket_list, ticket_id):
        city = LottoController.select_city()
        bet_type = LottoController.select_bet_type()
        amount_of_numbers = LottoController.select_amount_of_numbers(bet_type)
        cost = LottoController.select_cost()
        a_ticket = Ticket(city=city, bet_type=bet_type, amount_of_numbers=amount_of_numbers, cost=cost,
                          ticket_id=ticket_id)
        ticket_list.append(a_ticket)

    @staticmethod
    def create_extraction():
        return Extraction()

    @staticmethod
    def check_winning_ticket(ticket, extraction):
        winning_combinations = list()
        # cost_for_city = ticket.cost / len(ticket.city.)
        for city in ticket.city.get_name():
            print("$$check_winning_ticket: city: ", city)
            # city = ticket.city
            winning_numbers = list()
            for number in ticket.numbers:
                if number in extraction.drawn_numbers[city]:
                    winning_numbers.append(number)
            if len(winning_numbers) >= ticket.bet_type.min_amount_numbers:
                winning_combination = WinningCombination(city, ticket.bet_type, winning_numbers, len(ticket.numbers),
                                                         ticket.id)
                winning_combination.prize *= ticket.cost
                winning_combinations.append(winning_combination)
        return winning_combinations

    @staticmethod
    def calculate_winners(ticket_list, extraction):
        winners = []
        for i in range(len(ticket_list)):
            total_prize = 0
            winning = LottoController.check_winning_ticket(ticket_list[i], extraction)
            if len(winning) > 0:
                for w in winning:
                    # total_prize += w.prize * ticket_list[i].cost
                    total_prize += w.prize
                winner = Winner(winning, total_prize, ticket_list[i].id)
                winners.append(winner)
        return winners

        # ----------------------------------------------
        # if len(winning) > 0:
            # print("\n--- Winning: ticket n°", i+1)
            # winners.append(winning)
            # for w in winning:
                # LottoView.show_winners(w)
                # total_prize += w.prize * ticket_list[i].cost  # !!!
            # print("Total prize: €", total_prize)
        #---------------------------------------------------------------------------------        
        # return winners
    
    
if __name__ == '__main__':
    city_01 = City(all_cities=True)
    city_02 = City(all_cities=False, city=0)
    bet_type_01 = BetType(4)
    amount_of_numbers_01 = 10  # amount_of_numbers
    numbers_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_five = [1, 2, 3, 4, 5]
    t = Ticket(city_01, bet_type_01, amount_of_numbers_01, numbers_ten, cost=2, ticket_id=1)
    t_02 = Ticket(city_02, bet_type_01, amount_of_numbers_01, numbers_five, cost=2, ticket_id=2)


    # ex = LottoController.create_extraction()
    drawn_numbers = {'Bari': [1, 2, 3, 4, 5], 'Cagliari': [6, 7, 8, 9, 10], 'Firenze': [1, 3, 5, 7, 9],
                     'Genova': [13, 18, 11, 79, 17], 'Milano': [77, 48, 72, 84, 1], 'Napoli': [21, 81, 73, 87, 69],
                     'Palermo': [35, 36, 21, 12, 22], 'Roma': [11, 30, 7, 38, 24], 'Torino': [50, 4, 38, 9, 84],
                     'Venezia': [2, 4, 6, 8, 10]}
    ex = Extraction(drawn_numbers_=drawn_numbers)

    w_c = LottoController.check_winning_ticket(t, ex)
    w_c_02 = LottoController.check_winning_ticket(t_02, ex)

    LottoView.show_ticket(t, t.id)
    LottoView.show_ticket(t_02, t_02.id)
    LottoView.show_extraction(ex)
    for w in w_c:
        LottoView.show_winning_combination(w)
    for w_02 in w_c_02:
        LottoView.show_winning_combination(w_02)

    print('### Print show_winners ###')
    ticket_list = [t, t_02]
    winners = LottoController.calculate_winners(ticket_list, ex)
    LottoView.show_winners(winners)
