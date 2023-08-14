from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import time
import os

# Resource can be required for some backends, e.g. Jaeger
# If resource wouldn't be set - traces wouldn't appears in Jaeger
resource = Resource(attributes={
    "service.name": "service"
})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

JAEGER_GRPC_URL = os.getenv("JAEGER_GRPC_URL")
if( JAEGER_GRPC_URL == None ):
    JAEGER_GRPC_URL = "http://oops.wrong.com"
print("JAEGER_GRPC_URL = "+JAEGER_GRPC_URL)
otlp_exporter = OTLPSpanExporter(endpoint=JAEGER_GRPC_URL, insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)

trace.get_tracer_provider().add_span_processor(span_processor)



with tracer.start_as_current_span("foo"):
    time.sleep(0.1)
    print("func 1")
    with tracer.start_as_current_span("bar"):

        time.sleep(0.23)
        print("func 1.2")
        with tracer.start_as_current_span("db-call"):
            time.sleep(0.43)
            print("func 1.1.1")

    with tracer.start_as_current_span("bar"):
        time.sleep(0.23)
        print("func 1.3")

with tracer.start_as_current_span("xoo"):
    print("func 2")


with tracer.start_as_current_span("zoo"):
    print("func 3")
