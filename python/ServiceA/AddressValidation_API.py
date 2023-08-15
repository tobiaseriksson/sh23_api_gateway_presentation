import requests
from flask import Flask, request, __version__, jsonify, Response, Blueprint, make_response
import json
from Common import db
import time
import sys
import os

aggregator_api = Blueprint('aggregator_api', __name__)

print('Flask version = ' + __version__)

API_GATEWAY = os.getenv("API_GATEWAY")
if( API_GATEWAY == None ):
    API_GATEWAY = 'http://localhost:8080'
@aggregator_api.route('/aggregator/customer/<id>', methods=['GET'])
def api_customer(id):
    # print("ID = " + str(id))
    # query /api/indivdiual/<id>
    ind_req = requests.get(API_GATEWAY+"/sh23/api/addresses")
    if( ind_req.status_code != 200 ):
        errorMessage = "Oops, customer does not exists with id "+str(id)
        print(errorMessage, file=sys.stderr)
        return '{ "error": "'+errorMessage+'" }', 404

    # figure out address id
    indv = ind_req.json()
    address_id = indv['id']
    # query /api/address/<id>
    addr_req = requests.get(API_GATEWAY+"/sh23/api/addresses")
    if (addr_req.status_code != 200):
        errorMessage = "Oops, customer does not exists with id " + str(address_id)
        print(errorMessage, file=sys.stderr)
        return '{ "error": "'+errorMessage+'" }', 404
    addr = addr_req.json()

    # merge results
    summary = { "Name": indv['firstName']+" "+indv['lastName'], "address": addr['street']+" "+addr['city'] }

    return make_response( jsonify(summary), 200)


@aggregator_api.route('/3rd/validate', methods=['GET'])
def api_all_addresses():
    print(request.url)
    print(request.headers)
    response = { "message": "validation OK!" }
    return make_response(jsonify(response),200)
