from faker import Faker
import json
import random

from flask import Flask
from Service_A_API import service_a_api
from Service_B_API import service_b_api
from Service_C_API import service_c_api
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

app.register_blueprint(service_a_api)
app.register_blueprint(service_b_api)
app.register_blueprint(service_c_api)

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


port=5059
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=False)
