class Human:
    def __init__(self, name, surname, date, contact_telephone, city, country, home_address):
        self.name = name,
        self.surname = surname,
        self.date =date,
        self.contact_telephone = contact_telephone,
        self.city = city,
        self.country = country,
        self.home_address = home_address
    def SHUSHIN(self):
        try:
            return self.name, self.surname, self.date, self.contact_telephone, self.city, self.country, self.home_address
        except:
            print("No name, no surname, no date, no contact_telephone, no city, no country, no home_address")


a = Human("Georgiy", "Shushin", "29.02.2000", "907658234", "Tachkent", "Uzbekistan", "Prospect Shushina")
print(a.name, a.surname, a.date, a.contact_telephone, a.city, a.country, a.home_address)
