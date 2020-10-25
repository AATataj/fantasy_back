from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Boxscores
import socketio
import json, os

async_mode = None
basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode='eventlet')\
@sio.on('connection-bind')
def connection_bind(sid, data):
    ## code to capture data
    ## sid is unique for each connection and data is the additional
    ## info for the connection (roto, box, plays etc)

@sio.on('disconnect')
def test_disconnect(sid):
    ## code to capture data
    ## etc etc

# Create your views here.
@csrf_exempt
def dbQuery (request):
    queryData = json.load(request)
    print(queryData)
    print(queryData.get('name'))
    print(queryData.get('startDate'))
    print(queryData.get('endDate'))
    print(queryData.get('playerID'))

    queryResults = Boxscores.objects.filter(name = queryData.get('name'),
                                            date__lte= queryData.get('endDate'), 
                                            date__gte= queryData.get('startDate'),
                                            )


    print (str(len(queryResults)))
    print(queryResults[0].name + " " + str(queryResults[0].pts) + " " + str(queryResults[0].date))
    print(queryResults[1].name + " " + str(queryResults[1].pts) + " " + str(queryResults[1].date))
    jsonReply = serializers.serialize("json", queryResults)
    return JsonResponse(jsonReply, safe=False)
    # histatus = { "hiStatus" : "hellows" }
    # histatusJson = json.dumps(histatus)
    # return JsonResponse(histatusJson, safe=False)
