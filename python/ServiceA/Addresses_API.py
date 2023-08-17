from flask import Flask, request, __version__, jsonify, Response, Blueprint
import json
from Common import db
import time

addresses_api = Blueprint('addresses_api', __name__)

@addresses_api.route('/api/v1/addresses/<id>', methods=['GET'])
def api_addresses(id):
    # print("ID = " + str(id))
    addr = db.get_address(int(id))
    if (addr == None):
        return '{ "error": "Address with id ' + id + ' not found" }', 404
    return Response(json.dumps(addr.__dict__), mimetype='application/json')


@addresses_api.route('/api/v1/addresses', methods=['GET'])
def api_all_addresses():
    print(request.url)
    print(request.headers)
    return Response(json.dumps([obj.__dict__ for obj in db.get_all_addresses()]), mimetype='application/json')
