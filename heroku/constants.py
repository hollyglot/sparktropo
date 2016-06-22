#!/usr/bin/env python
import os

##
# itty -- a web framework
# 
# For simple HTTP requests.
# Set the "host" and "port" that Heroku requires for routing requests.


ITTY = {
    'host': '0.0.0.0',
    'port': int(os.environ.get('PORT', 8080))
}

##
# Authorization token for Spark. Required for working with Spark's API.
#
AUTH = "NGJjYjA2MTctNDlhMS00ZWE5LTllODMtODM5MjdjZGExNmM1NWQ1ZTI5ODEtYTcx"

##
# Request header for Spark Web API
#
HEADERS = {'Authorization':'Bearer ' + AUTH}

##
# Spark Web API URLs
#
BASE_URL = "https://api.ciscospark.com/v1/"
ROOMS_URL = BASE_URL+"rooms"
MESSAGES_URL = BASE_URL+"messages"
