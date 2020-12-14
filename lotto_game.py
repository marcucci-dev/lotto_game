from lotto.lotto_controller import LottoController
from lotto.lotto_view import LottoView


def main():
    num_of_tickets = LottoController.select_num_of_tickets()
    if num_of_tickets == 0:
        print("Exit")
        exit(0)
    else:
        '''ticket_list = []
        for i in range(num_of_tickets):
            print("-----\nTicket number", i + 1)
            LottoController.insert_ticket(ticket_list, i+1)'''
        ticket_list = LottoController.insert_tickets(num_of_tickets)

        # for ticket in ticket_list:
        for i in range(len(ticket_list)):
            LottoView.show_ticket(ticket_list[i], i+1)
            print()

        # make an extraction
        extraction = LottoController.create_extraction()
        LottoView.show_extraction(extraction)

        # for ticket in ticket_list check combinations wins
        winners = LottoController.calculate_winners(ticket_list, extraction)
        LottoView.show_winners(winners)

        print('\n'+'_'*80)
        main()


if __name__ == '__main__':
    main()
