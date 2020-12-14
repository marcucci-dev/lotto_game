class City:
    """Represents a city (aka 'ruota') of a ticket.

    Attributes:
        city: List[int]     is a List of indices for city_allowed list
    """
    # city_allowed = ["Tutte", "Bari", "Cagliari", "Firenze", "Genova",
    #                 "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]
    city_allowed = ["Bari", "Cagliari", "Firenze", "Genova",
                    "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

    def __init__(self, all_cities=True, city=0):
        """Initialize the value of a new city. If city parameter is not specified,
        then the value defaults to 0 (Tutte)."""
        self.city = []
        self.all_cities = all_cities
        if all_cities:
            for c in City.city_allowed:
                self.city.append(c)
        else:
            # print("***city", city)
            # print("***City.city_allowed[city]", City.city_allowed[city])
            self.city.append(City.city_allowed[city])

    # def get(self):
    #    return self.city

    def get_name(self):
        # return City.city_allowed[self.city]
        return self.city

    @staticmethod
    def get_max_index():
        return len(City.city_allowed) - 1

    @staticmethod
    def get_min_index():
        return 0
