import random
import uuid

from faker import Faker

from Address import Address
from Customer import Customer
from Individual import Individual
import re

class DataGenerator:
    def __init__(self):
        self.faker = Faker('en_US')

    def generate_individual(self,id):
        return Individual(id, str(uuid.uuid4()), self.faker.first_name(), self.faker.last_name(), self.faker.date_of_birth(None, 18, 80), self.faker.job())

    def generate_address(self,id):
        return Address(id, str(uuid.uuid4()), self.faker.country(), self.faker.city(), self.faker.street_name() + ' ' + str(random.randint(1, 70)), self.faker.postcode())

    def generate_customer(self,id,indv,addr) :
        email = self.generate_email(indv.firstName, indv.lastName, self.faker.domain_name(), id)
        return Customer(id, str(uuid.uuid4()), email, indv.id, addr.id )

    def generate_email(self, firstName, lastName, domain, num):
        email = firstName + "." + lastName + "_" + str(num) + "@" + domain
        return re.sub('[^0-9a-zA-Z.@_]+', '', email).lower()

