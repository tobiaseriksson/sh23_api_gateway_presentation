
# Sample API
This is a small REST API to help explain how you can work with the API Gateway

The datamodel is simple

* Customer
* Individual
* Address

The exposed API :
- GET /api/v1/individuals
- GET /api/v1/individuals/<id>
- GET /api/v1/addresses
- GET /api/v1/addresses/<id>
- GET /api/v1/emails
- GET /aggregator/customer/<email>
- GET /3rd/external/validate-address?street=<street>>&city=<city>
- POST /3rd/external/validate-address-with-post
- GET /api/v1/may-fail?fail=true||false
- GET /api/v1/may-take-time?timeout_ms=<ms>

The idea is that the API should be served by 4 different microservices

Individuals API
- GET /api/v1/individuals
- GET /api/v1/individuals/<id>
- GET /api/v1/may-fail?fail=true||false
- GET /api/v1/may-take-time?timeout_ms=<ms>

Address API
- GET /api/v1/addresses
- GET /api/v1/addresses/<id>

Aggregator API

- GET /aggregator/customer/<email>
- GET /api/v1/emails

Address Validation API
- GET /3rd/external/validate-address?street=<street>>&city=<city>
- POST /3rd/external/validate-address-with-post

## Build and Run
### Build Docker Image
> docker build --tag service_ab -f Dockerfile .

### Run / Start Docker 
> docker run --rm -p 5059:5059 --name ServiceA1 service_ab
