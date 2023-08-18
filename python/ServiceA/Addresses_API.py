from flask import Flask, request, __version__, jsonify, Response, Blueprint
import json
from Database import dbConn
from Address import Address

import time

addresses_api = Blueprint('addresses_api', __name__)

@addresses_api.route('/api/v1/addresses/<id>', methods=['GET'])
def api_addresses(id):
    # print("ID = " + str(id))
    addr = Address.get(int(id),dbConn())
    if (addr == None):
        return '{ "error": "Address with id ' + id + ' not found" }', 404
    return Response(json.dumps(addr.__dict__), mimetype='application/json')


@addresses_api.route('/api/v1/addresses', methods=['GET'])
def api_all_addresses():
    print(request.url)
    print(request.headers)
    return Response(json.dumps([obj.__dict__ for obj in Address.fetch_all(dbConn())]), mimetype='application/json')
