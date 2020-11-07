from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.models import Boxscores
import json

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

def Scraperoto(request):
    ## in here we'll need the function to call the scraper
    ## functions and get periodic results to push back to the front end

    # for now, let's just handle the request for the websocket and 
    # make sure it works with only a timer
    print (request)
    return
