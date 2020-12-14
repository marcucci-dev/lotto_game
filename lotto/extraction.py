from random import sample


class Extraction:
    """Represents a extraction of a lotto game.

    Attributes:
    -----------
        drawn_numbers: Dict[str, List[int]]
            is a dictionary of 10 elements where:
            * the key is a city and
            * the value is a list of 5 distinct integers between 1 and 90

        TBD???city: int     is a index for city_allowed list
    """
    city_list = ["Bari", "Cagliari", "Firenze", "Genova", "Milano",
                 "Napoli", "Palermo", "Roma", "Torino", "Venezia"]
    all_lotto_numbers = [i + 1 for i in range(90)]

    # def __init__(self, random_=True, drawn_numbers_=None):
    def __init__(self, drawn_numbers_=None) -> None:
        """Method
        If the drawn_numbers_ parameter is not provided, 5 random numbers are generated.

        Optional keyword arguments:
        Args:
            drawn_numbers_ (Dict[str, List[int]]):
        """
        if drawn_numbers_ is None:
            self.drawn_numbers = dict()
            for city in Extraction.city_list:
                self.drawn_numbers[city] = Extraction.random_generate(5)
        else:
            self.drawn_numbers = drawn_numbers_

    @staticmethod
    def random_generate(amount_of_numbers):
        return sample(Extraction.all_lotto_numbers, amount_of_numbers)


if __name__ == '__main__':
    drawn_numbers = {'Bari': [1, 2, 3, 4, 5], 'Cagliari': [63, 20, 62, 55, 84], 'Firenze': [52, 70, 81, 80, 41],
                     'Genova': [13, 18, 11, 79, 17], 'Milano': [77, 48, 72, 84, 1], 'Napoli': [21, 81, 73, 87, 69],
                     'Palermo': [35, 36, 21, 12, 22], 'Roma': [11, 30, 7, 38, 24], 'Torino': [50, 4, 38, 9, 84],
                     'Venezia': [41, 64, 70, 12, 83]}

    extraction_01 = Extraction(drawn_numbers_=drawn_numbers)
    print(extraction_01.drawn_numbers)

    extraction_02 = Extraction()
    print(extraction_02.drawn_numbers)
