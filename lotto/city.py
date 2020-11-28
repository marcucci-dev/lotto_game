class City:
    """Represents a city (aka 'ruota') of a ticket.

    Attributes:
        city: str ?
        city: int
    """
    city_allowed = ["Tutte", "Bari", "Cagliari", "Firenze", "Genova",
                    "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

    def __init__(self, city=0):
        """Initialize the value of a new city. If city parameter is not specified,
        then the value defaults to 0 (Tutte)."""
        self.set(city)
        pass
        '''if city in City.city_allowed:
            self.city = city
        else:
            raise ValueError(city+' is not a correct value')
        '''

    def set(self, city):
        if city in range(len(City.city_allowed)):
            self.__city = city
        else:
            # raise TypeError
            raise ValueError(f'The value {city} is out of range {0}..{len(City.city_allowed) - 1}')

        """try:
            # City(city_name)
            self.__city = city_name
        except ValueError as ve:
            print(f'You entered {city_name}, which is not a correct value. \nCity allowed are {City.city_allowed}')
        """

    def get(self):
        return self.__city

    def get_name(self):
        return City.city_allowed[self.__city]


def test():
    # city_01 = City("Roma")
    # city_02 = City("Roma")
    # city_02.set("Roma")
    city_03 = City()
    city_03.set(1)
    print("City value = ", city_03.get())
    print("City name = ", city_03.get_name())

    """city_name = "Bologna"
    try:
        city_01 = City(city_name)
    except ValueError as ve:
        print(f'You entered {city_name}, which is not a correct value. \nCity allowed are {City.city_allowed}')
    try:
        city_02 = City("Tutte")
    except:
        print("error")
    try:
        city_03 = City("Venezia")
    except:
        print("error")
    """


if __name__ == '__main__':
    test()
