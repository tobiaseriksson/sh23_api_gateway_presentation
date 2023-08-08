import json

class Individual:
    def __init__(self,id,firstName,lastName,dateOfBirth,job):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = str(dateOfBirth)
        self.job = job

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)