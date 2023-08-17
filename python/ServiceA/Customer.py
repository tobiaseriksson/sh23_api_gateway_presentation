import uuid

class Customer:
    def __init__(self,id,email,individual_id,address_id):
        self.id = id
        self.databaseId = str(uuid.uuid4())
        self.email = email
        self.individual_id = individual_id
        self.address_id = address_id
