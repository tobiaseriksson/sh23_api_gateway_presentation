from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import propagators


import os
import sys

# Resource can be required for some backends, e.g. Jaeger
# If resource wouldn't be set - traces wouldn't appears in Jaeger

SERVICE_NAME = os.getenv("SERVICE_NAME")
if( SERVICE_NAME == None ):
    SERVICE_NAME = 'Service'

resource = Resource(attributes={
    "service.name": SERVICE_NAME
})

traceProvider = TracerProvider(resource=resource)
trace.set_tracer_provider(traceProvider)
tracer = trace.get_tracer(__name__)

JAEGER_GRPC_URL = os.getenv("JAEGER_GRPC_URL")
if( JAEGER_GRPC_URL == None ):
    print("The env JAEGER_GRPC_URL was not set, and hence no Opentelemetry/Jaeger metrics/tracing can be sent",file=sys.stderr)
    JAEGER_GRPC_URL = "http://oops.wrong.com"
print("JAEGER_GRPC_URL = "+JAEGER_GRPC_URL)

otlp_exporter = OTLPSpanExporter(endpoint=JAEGER_GRPC_URL, insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)

traceProvider.add_span_processor(span_processor)
