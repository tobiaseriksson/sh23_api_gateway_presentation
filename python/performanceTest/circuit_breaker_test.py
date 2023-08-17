import time
from locust import HttpUser, task, between, constant_throughput, constant, LoadTestShape
import random

host_and_port = "http://192.168.1.245:8080"
# host_and_port = "http://192.168.10.99:8080"
# host_and_port = "http://localhost:8080" // Cannot use localhost when running from inside docker


class MyCustomShape(LoadTestShape):

    def tick(self):
        run_time = self.get_run_time()
        current_user_count = self.get_current_user_count()        
        # user_count, spawn_rate, user_classes = self.basic()        
        user_count, spawn_rate, user_classes = self.good_then_bad_then_good()        
        if( user_count != None ) :
            print("Tick: %.0f seconds, current = %d, target = %d, spawn-rate = %d, classes = %s" % (run_time,current_user_count,user_count, spawn_rate, user_classes)  )
            return (user_count, spawn_rate, user_classes)
        else:
            return None

    def basic(self):        
        user_count = 15
        spawn_rate = 1
        user_classes = [ BadAPISuccessRun ]
        return (user_count, spawn_rate, user_classes)

    def good_then_bad_then_good(self):
        run_time = self.get_run_time()
        user_count = 15
        spawn_rate = 1
        user_classes = [ ]

        if run_time <= 15 :
            user_classes = [ BadAPISuccessRun ]
            return (user_count, spawn_rate, user_classes)
        elif run_time > 15 and run_time <= 30:            
            user_classes = [ BadAPIFailRun ]
            return (user_count, spawn_rate, user_classes)
        if run_time > 30 and run_time <= 40: 
            user_classes = [ BadAPISuccessRun ]
            return (user_count, spawn_rate, user_classes)        
        else :
            # Ramp down to 0
            return None
            # (0, spawn_rate, user_classes)    

class BadAPISuccessRun(HttpUser):
    host = host_and_port
    wait_time = constant(1)

    @task
    def get_all_success(self):
        print("Should be ok.")
        self.client.get("/sh23/bad-api/individuals?fail=false", name="/sh23/api/individuals")    




class BadAPIFailRun(HttpUser):
    host = host_and_port
    wait_time = constant(1)

    @task
    def get_all_fail(self):
        print("Should fail !!!!!!")
        self.client.get("/sh23/bad-api/individuals?fail=true", name="/sh23/api/individuals")    

