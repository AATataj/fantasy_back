from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def dbQuery (request):
    print("we're in the dbQuery function...")
    print(json.load(request))
    histatus = { "hiStatus" : "hellows" }
    histatusJson = json.dumps(histatus)
    return JsonResponse(histatusJson, safe=False)