import time
from locust import HttpUser, task, between, constant_throughput, constant
import random

class QuickstartUser(HttpUser):

    host = "http://192.168.1.245:8080"
    # wait_time = between(1, 5)
    # wait_time = constant_throughput(0.1)
    # wait_time = constant_throughput(0.01)
    wait_time = constant(0.1)

    @task
    def test_get_one_individual(self):
        self.client.get("/sh23/api/individuals/"+str(random.randint(1,55)), name="/sh23/api/individuals/")


    def test_get_one_address(self):
        self.client.get("/sh23/api/addresses/"+str(random.randint(1,55)), name="/sh23/api/addresses/")
