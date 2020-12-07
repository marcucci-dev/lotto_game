class City:
    """Represents a city (aka 'ruota') of a ticket.

    Attributes:
        __city: int     is a index for city_allowed list
    """
    # city_allowed = ["Tutte", "Bari", "Cagliari", "Firenze", "Genova",
    #                 "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]
    city_allowed = ["Bari", "Cagliari", "Firenze", "Genova",
                    "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

    def __init__(self, all_cities=True, city=0):
        """Initialize the value of a new city. If city parameter is not specified,
        then the value defaults to 0 (Tutte)."""
        self.__city = []
        self.all_cities = all_cities
        if all_cities:
            for c in City.city_allowed:
                self.__city.append(c)
        else:
            # print("***city", city)
            # print("***City.city_allowed[city]", City.city_allowed[city])
            self.__city.append(City.city_allowed[city])
        pass
        '''if city in City.city_allowed:
            self.city = city
        else:
            raise ValueError(city+' is not a correct value')
        '''

    def __set(self, city):
        if city in range(len(City.city_allowed)):
            self.__city = city
        else:
            # raise TypeError
            raise ValueError(f'The value {city} is out of range {City.get_min_index()}..{City.get_max_index()}')

        """try:
            # City(city_name)
            self.__city = city_name
        except ValueError as ve:
            print(f'You entered {city_name}, which is not a correct value. \nCity allowed are {City.city_allowed}')
        """

    def get(self):
        return self.__city

    def get_name(self):
        # return City.city_allowed[self.__city]
        return self.__city

    @staticmethod
    def get_max_index():
        return len(City.city_allowed) - 1

    @staticmethod
    def get_min_index():
        return 0


def test():

    for i in range(City.get_max_index()+1):
        city_01 = City(i)
        assert city_01.get_name() == City.city_allowed[city_01.get()]
        print("City value = ", city_01.get())
        print("City name = ", city_01.get_name())

    city_02 = City()
    print("City value =", city_02.get())
    print("City name =", city_02.get_name())


if __name__ == '__main__':
    test()
