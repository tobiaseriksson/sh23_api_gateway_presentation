import random

from faker import Faker

from Address import Address
from Customer import Customer
from Individual import Individual


class DataGenerator:
    def __init__(self):
        self.faker = Faker('en_US')

    def generate_individual(self,id):
        return Individual(id, self.faker.first_name(), self.faker.last_name(), self.faker.date_of_birth(None, 18, 80), self.faker.job())


    def generate_address(self,id):
        return Address(id, self.faker.country(), self.faker.city(), self.faker.street_name() + ' ' + str(random.randint(1, 70)), self.faker.postcode())

    def generate_customer(self,id,individual_id,address_id) :
        return Customer(id, self.faker.ascii_email(), individual_id, address_id )