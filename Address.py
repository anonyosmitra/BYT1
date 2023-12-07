class Address:

    def __init__(self, street, postal_code, city, country, phone_number):
        self.street = street
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}, {self.country}, {self.phone_number}"
