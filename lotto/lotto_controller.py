from city import City
from bet_type import BetType
from ticket import Ticket
from extraction import Extraction
from winning_combination import WinningCombination

class LottoController:
    @staticmethod
    def check_input(prompt, min_value, max_value, range_=None):
        """Read a string from standard input until an integer value is provided
        within the bounds min_value and max_value.
        The prompt string is printed to standard output before reading input.
        Returns an integer entered by the user between min_value and max_value.

        Args:
            prompt: string
            min_value :  int
            max_value:   int
            range_:

        Returns:
            user_input: int
        """
        while True:
            user_input = input(prompt)
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
            else:
                return user_input

    @staticmethod
    def select_num_of_tickets():
        prompt = "How many tickets do you want to generate (min: 1, max: 5, exit: 0) \n"
        # range_ = range(10)
        return LottoController.check_input(prompt, min_value=0, max_value=5)

    @staticmethod
    def select_city():
        suffix = ""
        for j in range(City.get_max_index()+1):
            suffix += "\n\t" + str(j) + ": " + City.city_allowed[j] + " "
        prompt = "Choose the \"city\" (aka \"ruota\"): " + suffix + "\n"
        city_index = LottoController.check_input(prompt, min_value=City.get_min_index(), max_value=City.get_max_index())
        a_city = City(city_index)
        return a_city

    @staticmethod
    def select_bet_type():
        suffix = ""
        for j in range(BetType.get_max_index()+1):
            suffix += "\n\t" + str(j+1) + ": " + str(BetType.bet_type_allowed[j]) + " "
        prompt = "Choose the type of bet:" + suffix + "\n"
        bet_type = LottoController.check_input(prompt, min_value=BetType.get_min_index() + 1, max_value=BetType.get_max_index() + 1)
        a_bet_type = BetType(bet_type-1)
        return a_bet_type

    @staticmethod
    def select_amount_of_numbers(bet_type):
        min_for_bet_type = bet_type.get()+1
        max_for_bet_type = 10
        prompt = "Choose the amount of numbers to generate (min {} max {} per this bet) \n".format(min_for_bet_type,
                                                                                                   max_for_bet_type)
        return LottoController.check_input(prompt, min_value=min_for_bet_type, max_value=10)

    @staticmethod
    def insert_ticket(ticket_list, ticket_id):
        city = LottoController.select_city()
        bet_type = LottoController.select_bet_type()
        amount_of_numbers = LottoController.select_amount_of_numbers(bet_type)
        a_ticket = Ticket(city=city, bet_type=bet_type, amount_of_numbers=amount_of_numbers, ticket_id=ticket_id)
        ticket_list.append(a_ticket)

    @staticmethod
    def create_extraction():
        return Extraction()

    @staticmethod
    def check_winning_ticket(ticket, extraction):
        winning_combinations = list()
        # for city in ticket.city:
        if True:
            city = ticket.city
            winning_numbers = list()
            for number in ticket.numbers:
                if number in extraction.drawn_numbers[city.get_name()]:
                    winning_numbers.append(number)
            if len(winning_numbers) >= ticket.bet_type.min_amount_numbers:
                winning_combination = WinningCombination(city, ticket.bet_type, winning_numbers, 1)
                winning_combinations.append(winning_combination)
        return winning_combinations


if __name__ == '__main__':
    # bet_type_01 = LottoController.select_bet_type()
    # print(bet_type_01.get_name())

    city_01 = City(1)  # manca il caso TUTTE
    bet_type_01 = BetType(0)
    amount_of_numbers_01 = 10  # amount_of_numbers
    t = Ticket(city_01, bet_type_01, amount_of_numbers_01)
    
    ex = LottoController.create_extraction()

    w_c = LottoController.check_winning_ticket(t, ex)
    for w in w_c:
        print(w)

        print(1, w.city, w.bet_type, w.winning_numbers)
        print(w.city.get_name())
        print(w.bet_type.get_name())
        print(w.winning_numbers)
        print(w.amount_winning_combinations)



    
    
