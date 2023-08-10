import uuid

class Address:
    def __init__(self,id,country,city,street,zipcode):
        self.id = id
        self.databaseId = str(uuid.uuid4())
        self.country = country
        self.city = city
        self.street = street
        self.zipcode = zipcode
