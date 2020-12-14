from lotto.lotto_controller import LottoController
from lotto.lotto_view import LottoView


def main():
    num_of_tickets = LottoController.select_num_of_tickets()
    if num_of_tickets == 0:
        print("Exit")
        exit(0)
    else:
        # make tickets
        ticket_list = LottoController.insert_tickets(num_of_tickets)
        LottoView.show_tickets(ticket_list)

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
