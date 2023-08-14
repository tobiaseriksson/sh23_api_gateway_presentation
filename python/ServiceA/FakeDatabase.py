from opentelemtetry import tracer
from typing import List
from faker import Faker
from Address import Address
from Individual import Individual

class FakeDatabase:
    def __init__(self):
        self.faker = Faker('en_US')
        self.individuals:List[Individual] = []
        self.addresses:List[Address] = []

    def add_Individual(self,indv:Individual):
        self.individuals.append(indv)

    def get_individual(self,id:int):
        for indv in self.individuals:
            if indv.id == id:
                return indv
        return None

    def get_all_individuals(self):
        with tracer.start_as_current_span('db-get-all-individuals'):
            return self.individuals

    def add_address(self,addr:Address):
        self.addresses.append(addr)

    def get_address(self,id:int):
        for addr in self.addresses:
            if( addr.id == id ):
                return addr
        return None

    def get_all_addresses(self):
        return self.addresses

