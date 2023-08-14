from flask import Flask, request, __version__, jsonify, Response, Blueprint
import json
from Common import db
from opentelemtetry import tracer, trace
import requests

import time
from datetime import datetime

service_a_api = Blueprint('service_a_api', __name__)

print('Flask version = ' + __version__)

@service_a_api.route('/api/may-fail', methods=['GET'])
def api_may_fail():
    fail = request.args.get('fail')
    if( fail != None and fail.lower() == 'true') :
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        return '{ "error": "['+dt_string+'] request failed for some reason..." }', 404

    return Response(json.dumps([obj.__dict__ for obj in db.get_all_individuals()]), mimetype='application/json')


@service_a_api.route('/api/may-take-time', methods=['GET'])
def api_may_take_time():
    with tracer.start_as_current_span('/api/may-take-time'):
        timeout = request.args.get('timeout')
        if( timeout != None ) :
            print("Sleeping for "+timeout+" seconds ... ")
            with tracer.start_as_current_span('sleeping'):
                time.sleep(int(timeout))
        else:
            print("No timeout")
        return Response(json.dumps([obj.__dict__ for obj in db.get_all_individuals()]), mimetype='application/json')

@service_a_api.route('/api/individuals', methods=['GET'])
def api_all_individual():
    print(request.url)
    print(request.headers)
    ctx = trace.get_current_span().get_span_context()

    print("SpanId = "+hex(ctx.span_id))
    print("TraceId = "+hex(ctx.trace_id))
    with tracer.start_as_current_span('call-to-get-addresses'):
        r = requests.get("http://localhost:8080/sh23/api/addresses")
        print("data : "+r.text)
    return Response(json.dumps([obj.__dict__ for obj in db.get_all_individuals()]), mimetype='application/json')


@service_a_api.route('/api/individuals/<id>', methods=['GET'])
def api_individual(id):
    # print("ID = " + str(id))
    indv = db.get_individual(int(id))
    if (indv == None):
        return '{ "error": "Individual with id ' + id + ' not found" }', 404
    return Response(json.dumps(indv.__dict__), mimetype='application/json')

