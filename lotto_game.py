from lotto.lotto_controller import LottoController
from lotto.lotto_view import LottoView


def main():
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
        '''
        winners = []
        for i in range(len(ticket_list)):
        #---------------------------------------------------------------------------------
            total_prize = 0
            winning = LottoController.check_winning_ticket(ticket_list[i], extraction)
            if len(winning) > 0:
                print("\n--- Winning: ticket n°", i+1)
                winners.append(winning)
                for w in winning:
                    LottoView.show_winning_combination(w)
                    total_prize += w.prize * ticket_list[i].cost  # !!!
                print("Total prize: €", total_prize)
        #---------------------------------------------------------------------------------

        if len(winners) == 0:
            print("\n# Sorry, no winning tickets...")
        '''
        winners = LottoController.calculate_winners(ticket_list, extraction)
        LottoView.show_winners(winners)

        '''if len(winners) == 0:
            print("\n# Sorry, no winning tickets...")
        else:
            for w in winners:
                for comb in w:
                    LottoView.show_winning_combination(comb)
        '''
        print('\n'+'_'*80)
        main()


if __name__ == '__main__':
    main()
