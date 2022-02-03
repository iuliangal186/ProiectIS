""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /fereastra, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fereastra"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("last_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/fereastra"
)
req_collection.add_request(request)

# Endpoint: /fereastra, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fereastra"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/fereastra"
)
req_collection.add_request(request)

# Endpoint: /usa, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("usa"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("last_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/usa"
)
req_collection.add_request(request)

# Endpoint: /usa, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("usa"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/usa"
)
req_collection.add_request(request)

# Endpoint: temperatura, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperatura"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="temperatura"
)
req_collection.add_request(request)

# Endpoint: /temperatura/statistics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("temperatura"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statistics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("time_period="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/temperatura/statistics"
)
req_collection.add_request(request)

# Endpoint: /lumina, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lumina"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lumina"
)
req_collection.add_request(request)

# Endpoint: /lumina/statistics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lumina"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statistics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("time_period="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/lumina/statistics"
)
req_collection.add_request(request)

# Endpoint: /umiditate, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("umiditate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/umiditate"
)
req_collection.add_request(request)

# Endpoint: /umiditate/statistics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("umiditate"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statistics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("time_period="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/umiditate/statistics"
)
req_collection.add_request(request)

# Endpoint: /miscare, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("miscare"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/miscare"
)
req_collection.add_request(request)

# Endpoint: /miscare/statistics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("miscare"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statistics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("time_period="),
    primitives.restler_fuzzable_number("1.23"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/miscare/statistics"
)
req_collection.add_request(request)

# Endpoint: /vreme, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("vreme"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:42178\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/vreme"
)
req_collection.add_request(request)
