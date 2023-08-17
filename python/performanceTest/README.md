# Locus for Performance Testing

## Download Locust Docker
> docker pull locustio/locust

## Run locust Docker 
>  docker run --rm --name Locust -v $(pwd):/mnt/locust -p 8089:8089 locustio/locust -f /mnt/locust/locustfile.py

## Web Control Center
Once the docker is started, go to 
http://0.0.0.0:8089/

E.g.

Number of Users : 5 (some sort of max parallelism)
Spawn Rate : 5 (controls how quickly it will reach the peak)