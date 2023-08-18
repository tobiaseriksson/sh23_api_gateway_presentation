
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

