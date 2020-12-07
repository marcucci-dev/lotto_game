# from lotto.city import City
# from lotto.bet_type import BetType
# from lotto.ticket import Ticket

from lotto.lotto_controller import LottoController
from lotto.lotto_view import LottoView


def main():
    # c = LottoController(ModelBasic(my_items), View())

    # global ticket
    num_of_tickets = LottoController.select_num_of_tickets()
    if num_of_tickets == 0:
        print("Exit")
        exit(0)
    else:
        ticket_list = []
        for i in range(num_of_tickets):
            print("-----\nTicket number", i + 1)
            LottoController.insert_ticket(ticket_list, i+1)

        # for ticket in ticket_list:
        for i in range(len(ticket_list)):
            LottoView.show_ticket(ticket_list[i], i+1)
            print()

        # make an extraction
        extraction = LottoController.create_extraction()
        LottoView.show_extraction(extraction)

        # for ticket in ticket_list check combinations wins
        winners = []
        for i in range(len(ticket_list)):
            winning = LottoController.check_winning_ticket(ticket_list[i], extraction)
            if len(winning) > 0:
                print("\n--- Winning: ticket ", i+1)
                winners.append(winning)
                for w in winning:
                    LottoView.show_winners(w)
        if len(winners) == 0:
            print("\n# Sorry, no winning tickets...")
        print('\n'+'_'*80)
        main()


if __name__ == '__main__':
    main()
