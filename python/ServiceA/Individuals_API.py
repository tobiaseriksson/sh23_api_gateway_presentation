from flask import Flask, request, __version__, jsonify, Response, Blueprint, make_response
import json
from Common import db
from opentelemtetry import tracer, trace
import requests

import time
from datetime import datetime

individuals_api = Blueprint('individuals_api', __name__)

@individuals_api.route('/api/v1/may-fail', methods=['GET'])
def api_may_fail():
    fail = request.args.get('fail')
    if (fail != None and fail.lower() == 'true'):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        err = [ {"error": "["+dt_string+"] request failed for some reason..."} ]
        return jsonify(err), 400
    return jsonify( [obj.__dict__ for obj in db.get_all_individuals()]), 200

@individuals_api.route('/api/v1/may-take-time', methods=['GET'])
def api_may_take_time():
    with tracer.start_as_current_span('/api/may-take-time'):
        timeout = request.args.get('timeout_ms')
        if (timeout != None):
            print("Sleeping for " + timeout + " ms ... ")
            with tracer.start_as_current_span('sleeping'):
                time.sleep(int(timeout) / 1000)
        else:
            print("No timeout")
        return Response(json.dumps([obj.__dict__ for obj in db.get_all_individuals()]), mimetype='application/json')


@individuals_api.route('/api/v1/individuals', methods=['GET'])
def api_all_individual():
    print(request.url)
    print(request.headers)
    ctx = trace.get_current_span().get_span_context()

    print("SpanId = " + hex(ctx.span_id))
    print("TraceId = " + hex(ctx.trace_id))
    return Response(json.dumps([obj.__dict__ for obj in db.get_all_individuals()]), mimetype='application/json')


@individuals_api.route('/api/v1/individuals/<id>', methods=['GET'])
def api_individual(id):
    # print("ID = " + str(id))
    indv = db.get_individual(int(id))
    if (indv == None):
        return '{ "error": "Individual with id ' + id + ' not found" }', 404
    return Response(json.dumps(indv.__dict__), mimetype='application/json')
