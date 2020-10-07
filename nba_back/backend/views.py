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
    print(queryData.get('name'))
    print(queryData.get('startDate'))
    print(queryData.get('endDate'))
    print(queryData.get('playerID'))

    queryResults = Boxscores.objects.filter(name = queryData.get('name'),
                                            date__lte= queryData.get('endDate'), 
                                            date__gte= queryData.get('startDate'),
                                            )[:5]


    print (str(len(queryResults)))
    print(queryResults[0].name + " " + str(queryResults[0].pts) + " " + str(queryResults[0].date))
    print(queryResults[1].name + " " + str(queryResults[1].pts) + " " + str(queryResults[1].date))
    jsonReply = serializers.serialize("json", queryResults)
    return JsonResponse(jsonReply, safe=False)
    # histatus = { "hiStatus" : "hellows" }
    # histatusJson = json.dumps(histatus)
    # return JsonResponse(histatusJson, safe=False)