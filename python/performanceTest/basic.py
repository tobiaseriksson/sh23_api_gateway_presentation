import time
from locust import HttpUser, task, between, constant_throughput, constant, LoadTestShape
import random


# host_and_port = "http://192.168.1.245:8080"
host_and_port = "http://172.20.10.13:8080"
# host_and_port = "http://192.168.10.99:8080"
# host_and_port = "http://localhost:8080" // Cannot use localhost when running from inside docker

class BasicTasks(HttpUser):
    host = host_and_port
    # wait_time = between(1, 5)
    # wait_time = constant_throughput(0.1)
    # wait_time = constant_throughput(0.01)
    wait_time = constant(0.2)

    @task
    def test_get_one_individual(self):
        self.client.get("/sh23/api/individuals/"+str(random.randint(1,55)), name="/sh23/api/individuals/<id>")

    def test_get_one_address(self):
        self.client.get("/sh23/api/addresses/"+str(random.randint(1,55)), name="/sh23/api/addresses/")

    def test_first_ok_then_fail_then_ok(self):
        runtime = self.get
