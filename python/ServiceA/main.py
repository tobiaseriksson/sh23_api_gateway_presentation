from faker import Faker
import json
import random

from flask import Flask, __version__
from Individuals_API import individuals_api
from Addresses_API import addresses_api
from Aggregator_API import aggregator_api
from AddressValidation_API import addressvalidation_api

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app = Flask(__name__)
app.debug = True
print('Flask version = ' + __version__)

app.register_blueprint(individuals_api)
app.register_blueprint(addresses_api)
app.register_blueprint(aggregator_api)
app.register_blueprint(addressvalidation_api)

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


port=5059
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
