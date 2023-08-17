import requests
from flask import Flask, request, __version__, jsonify, Response, Blueprint, make_response
import json
from Common import db
import time
import sys
import os

aggregator_api = Blueprint('aggregator_api', __name__)

API_GATEWAY = os.getenv("API_GATEWAY")
if( API_GATEWAY == None ):
    API_GATEWAY = 'http://localhost:8080'
print("API_GATEWAY = "+API_GATEWAY)

@aggregator_api.route('/aggregator/customer/<email>', methods=['GET'])
def api_customer(email):
    print("get ONE customer!")

    # Query database for Customer
    customer = db.get_customer_by_email(email)
    if (customer == None):
        return '{ "error": "Customer with id ' + email + ' not found" }', 404

    # query Individuals API
    individual_id = customer.individual_id
    ind_req = requests.get(API_GATEWAY + "/sh23/api/individuals/"+str(individual_id))
    if (ind_req.status_code != 200):
        errorMessage = "Oops, individual does not exists with id " + str(id)
        print(errorMessage, file=sys.stderr)
        return '{ "error": "' + errorMessage + '" }', 404

    # query Addresses API
    address_id = customer.address_id
    address_req = requests.get(API_GATEWAY+"/sh23/api/addresses/"+str(address_id))
    if( address_req.status_code != 200 ):
        errorMessage = "Oops, customer does not exists with id "+str(id)
        print(errorMessage, file=sys.stderr)
        return '{ "error": "'+errorMessage+'" }', 404

    # figure out address id
    indv = ind_req.json()
    addr = address_req.json()

    # merge results
    summary = { "email": customer.email, "name": indv['firstName']+" "+indv['lastName'], "address": addr['street']+", "+addr['city']+", "+addr['country'] }

    return make_response( jsonify(summary), 200)

@aggregator_api.route('/api/v1/emails', methods=['GET'])
def api_all_customers():
    print(request.url)
    print(request.headers)
    return Response(json.dumps([obj.__dict__['email'] for obj in db.get_all_customers()]), mimetype='application/json')
