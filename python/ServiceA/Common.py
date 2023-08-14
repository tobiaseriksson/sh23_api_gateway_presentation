
from DataGenerator import DataGenerator
from FakeDatabase import FakeDatabase

data_generator = DataGenerator()
db = FakeDatabase()

number_of_customers = 100
for id in range(number_of_customers):
    db.add_Individual(data_generator.generate_individual(id))
    db.add_address(data_generator.generate_address(id))

print(str(number_of_customers)+' customers generated')


