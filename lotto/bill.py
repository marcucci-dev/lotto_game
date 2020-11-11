import random

import table


class Bill:
    """Represents a bill of the lotto game.

    attributes: type: integer 0-4
                numbers: list of int
                city: integer 0-10
                # cost: double (not in Learning Path level 1)

                table_layout: object to print the generated tickets with nice ascii art table decoration.
    """
    type_names = ["ambata", "ambo", "terno", "quaterna", "cinquina"]
    city_names = ["Tutte", "Bari", "Cagliari", "Firenze", "Genova",
                  "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

    def __init__(self, bill_type=0, amount_of_numbers=10, city=0):
        self.type = bill_type
        self.numbers = self.generate_numbers(amount_of_numbers)
        self.city = city
        self.table_layout = table.TableLayout()
        self.table_layout.set_fields_names(["Numbers", "Ruota", "Type"])
        if self.check_type() and self.check_numbers() and self.check_city():
            self.table_layout.set_fields_values((self.list_number_to_str(), Bill.city_names[self.city],
                                                 Bill.type_names[self.type]))
        else:
            raise Exception("Sorry, Bill.__init__ raise an exception")

        self.table_layout.set_fields_widths()

    def __str__(self):
        """Returns a human-readable string representation."""
        """return '{type} of {amount_of_numbers} numbers on {city} ruota: ' \
               '\n\t{numbers}'.format(type=Bill.type_names[self.type], city=Bill.city_names[self.city],
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

    def check_type(self):
        is_valid = 0 <= self.type < len(self.type_names)
        if not is_valid:
            print("The self.type = {:d} is out of range [0..{:d}]".format(self.type, len(self.type_names) - 1))
        return is_valid

    def check_city(self):
        is_valid = 0 <= self.city < len(self.city_names)
        if not is_valid:
            print("The self.city = {:d} is out of range [0..{:d}]".format(self.city, len(self.city_names) - 1))
        return is_valid

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
        type_is_valid = self.check_type()
        city_is_valid = self.check_city()
        numbers_are_valid = self.check_numbers()
        return type_is_valid and numbers_are_valid and city_is_valid

    def list_number_to_str(self):
        out = ""
        for num in self.numbers:
            out += str(num) + " "
        return out


if __name__ == '__main__':
    # make a bill
    bill = Bill()
    bill.generate_numbers(5)
    print(bill)
    assert bill.validate()

    """bill_02 = Bill(5, 1, 5)
    assert not bill_02.validate()

    bill_03 = Bill(4, 1, 11)
    assert not bill_03.validate()

    bill_04 = Bill(4, 0, 10)
    assert not bill_04.validate()

    bill_05 = Bill(4, 11, 10)
    assert not bill_05.validate()

    bill_06 = Bill()
    bill_06.numbers = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]
    assert not bill_06.validate()

    bill_07 = Bill()
    bill_07.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 90, 90]
    assert not bill_07.validate()
    """
