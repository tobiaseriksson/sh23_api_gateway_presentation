import requests
from flask import Flask, request, __version__, jsonify, Response, Blueprint, make_response
import json
import time
import sys
import os
import random

addressvalidation_api = Blueprint('addressvalidation_api', __name__)


def validate_address(city,street):
    response_code = 200
    if (street == None or city == None):
        response_code = 400
        response = {"message": "Both parameter; street and city needs to be present!"}
    elif (random.randint(0, 1) > 0):
        response = {"success": True, "message": "validation OK!", "data": {"street": street, "city": city}}
    else:
        response = {"success": False, "message": "not a proper address!", "data": {"street": street, "city": city}}
    return response, response_code

#
# GET /3rd/external/validate-address?street=<street>&city=<city>
# Parameters
# - street
# - city
#
# Returns HTTP 200 on both valid and not valid , 400 on failure
# {
#     "data": {
#         "city": "norrköping",
#         "street": "storgatan 99"
#     },
#     "message": "not a proper address!",
#     "success": false
# }
@addressvalidation_api.route('/3rd/external/validate-address', methods=['GET'])
def api_validate_address():
    print(request.url)
    print(request.headers)

    street = request.args.get('street')
    city = request.args.get('city')

    response, response_code = validate_address(city,street)
    return make_response(jsonify(response), response_code)


#
# POST /3rd/external/validate-address-with-post
# Body is expected like this
# {
#     "city": "norrköping",
#     "street": "storgatan 99"
# }
#
# Returns HTTP 200 on both valid and not valid , 400 on failure
# {
#     "data": {
#         "city": "norrköping",
#         "street": "storgatan 99"
#     },
#     "message": "not a proper address!",
#     "success": false
# }
@addressvalidation_api.route('/3rd/external/validate-address-with-post', methods=['POST'])
def address_validation_with_post():
    print("URL: "+request.url)
    print("Headers: \n"+str(request.headers))
    print("Parameters: "+str(request.args))
    print("Data: \n"+str(request.data))

    jsonObj = request.json

    city = jsonObj['city']
    street = jsonObj['street']

    response, response_code = validate_address(city, street)
    return make_response(jsonify(response), response_code)
