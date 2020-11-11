import lotto.bill


def check_input(prompt, range_, min_, max_):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except ValueError:
            print("Input type must be int\n")
            continue

        # if user_input not in range_:
        #    print("Input must be in range [{0.start}..{0.stop}).\n".format(range_))
        # print("min e max", min_, max_)
        if user_input < min_:
            print("Input must be greater than or equal to {0}.\n".format(min_))
        elif user_input > max_:
            print("Input must be less than or equal to {0}.\n".format(max_))
        else:
            return user_input


def select_num_of_bills():
    prompt = "How many bills do you want to generate (min: 1, max: 5, exit: 0) \n"
    range_ = range(10)
    return check_input(prompt, range_, 0, 5)


def select_bill_type():
    suffix = ""
    for j in range(len(lotto.bill.Bill.type_names)):
        suffix += "\n\t" + str(j) + ": " + lotto.bill.Bill.type_names[j] + " "
    prompt = "Choose the type of bill:" + suffix + "\n"

    range_ = range(len(lotto.bill.Bill.type_names))
    return check_input(prompt, range_, 0, len(lotto.bill.Bill.type_names) - 1)


def select_amount_of_numbers():
    prompt = "Choose the amount of numbers to generate (max 10 per bill) \n"
    range_ = range(10)
    return check_input(prompt, range_, 1, 10)


def select_bill_city():
    suffix = ""
    for j in range(len(lotto.bill.Bill.city_names)):
        suffix += "\n\t" + str(j) + ": " + lotto.bill.Bill.city_names[j] + " "
    prompt = "Choose the \"city\" (aka \"ruota\") of the bill: " + suffix + "\n"

    range_ = range(len(lotto.bill.Bill.city_names))
    return check_input(prompt, range_, 0, len(lotto.bill.Bill.city_names) - 1)


if __name__ == '__main__':
    num_of_bills = select_num_of_bills()

    if num_of_bills == 0:
        print("Exit")
        exit(0)
    else:
        bill_list = []
        for i in range(num_of_bills):
            print("-----\nBill number", i+1)
            bill_type = select_bill_type()
            amount_of_numbers = select_amount_of_numbers()
            city = select_bill_city()

            a_bill = lotto.bill.Bill(bill_type, amount_of_numbers, city)
            bill_list.append(a_bill)

        for bill in bill_list:
            print(bill)
