#!/usr/bin/env python
from constants import ITTY, HEADERS, ROOMS_URL, MESSAGES_URL
from itty import *
import requests
import json
import urllib

##
# Post request to Spark Web API to create Devs room
#
def create_devs_room():
    data = {"title" : "Devs"}
    resp = requests.post(ROOMS_URL,json=data, headers=HEADERS)
    return json.loads(resp.text)['id']

##
# Check rooms dictionary for Devs room
#
def get_devs_id(rooms):
    devs_id = ''.join([r['id'] for r in rooms if r['title'] == "Devs"])
    if len(devs_id) > 0:
        return devs_id
    else:
        raise Exception("Dev room has not been created.")

##
# Create Devs room on Spark
#
def setup():
    resp = requests.get(ROOMS_URL, headers=HEADERS)
    rooms = json.loads(resp.text)['items']
    try:
        return get_devs_id(rooms)
    except:
        return create_devs_room()


##
# Setup up Spark and get Devs room id
#
DEVS_ID = setup()

##
# Posts message to Devs room on Spark
#
def send_message(room_id, message):
    data = { "roomId" : room_id,
             "text" : message }
    resp = requests.post(MESSAGES_URL,json=data, headers=HEADERS)
    return json.loads(resp.text)

##
# Path : /messages
# Method : POST
#
# This path receives the text message posted from Tropo.
#
@post('/messages')
def _(request):
    message = request.body
    response = send_message(DEVS_ID, message)
    return Response(json.dumps(response), content_type='application/json')


run_itty(**ITTY)