from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import StationInfo
import requests
import json
from mymetro.settings_secret import api_wmata_key

# def index(request):
#     latest_trains = StationInfo.objects.order_by('car_db')
#     output = ','.join([t.destinationCode_db+" "+t.destinationName_db for t in latest_trains])
#     return HttpResponse("This is the first response from the view: %s " % output)


def index(request):
    latest_trains = StationInfo.objects.order_by('car_db')
    template = loader.get_template('trains/index.html')
    url_FB = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/D05"
    url_CS = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/C04"
    key = api_wmata_key
    headers = { "api_key" : key, "Content-Type" : "application/json"}
    req_FB = requests.get(url_FB, headers = headers)
    req_CS = requests.get(url_CS, headers = headers)
    content_FB = req_FB.content
    content_CS = req_CS.content
    trains_FB = json.loads(content_FB.decode("utf-8"))
    trains_CS = json.loads(content_CS.decode("utf-8"))
    context = {
        'latest_trains': latest_trains,
        'trains_FB': trains_FB['Trains'],
        'trains_CS': trains_CS['Trains']
    }
    return HttpResponse(template.render(context,request))

def trainDetails(request, locationCode_db):
    return HttpResponse("This is the value in car db %s" % locationCode_db)

