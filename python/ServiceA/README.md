
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


## Database 
### Create Database and Tables

```
DROP TABLE IF EXISTS "address";
CREATE TABLE "public"."address" (
    "id" integer NOT NULL,
    "database_id" character varying(50) NOT NULL,
    "country" character varying(100) NOT NULL,
    "city" character varying(100) NOT NULL,
    "street" character varying(100) NOT NULL,
    "zipcode" character varying(100) NOT NULL,
    CONSTRAINT "address_database_id" UNIQUE ("database_id"),
    CONSTRAINT "address_id" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "customer";
CREATE TABLE "public"."customer" (
    "id" integer NOT NULL,
    "database_id" character varying(50) NOT NULL,
    "email" character varying(50) NOT NULL,
    "individual_id" integer NOT NULL,
    "address_id" integer NOT NULL,
    CONSTRAINT "customer_database_id" UNIQUE ("database_id"),
    CONSTRAINT "customer_id" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "individual";
CREATE TABLE "public"."individual" (
    "id" integer NOT NULL,
    "database_id" uuid NOT NULL,
    "first_name" character varying(50) NOT NULL,
    "last_name" character varying(50) NOT NULL,
    "date_of_birth" date NOT NULL,
    "job" character varying(100) NOT NULL,
    CONSTRAINT "individual_database_id" UNIQUE ("database_id"),
    CONSTRAINT "individual_id" PRIMARY KEY ("id")
) WITH (oids = false);

```


### Import data into the database
Either run the database_data.sql file with all the INSERTs
or run the fill_database() in the Database.py file.
