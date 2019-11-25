import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response

from dashboard.models import Compaign
from dashboard.algorithms import populate_database, query_database
from dashboard.constants import DATA_DIR, DATA_FILE_NAME, BASE_DIR

# Dashboard display
def index(request):
    return render_to_response("index.html", {"compaigns": json.dumps(list(Compaign.objects.values()), cls=DjangoJSONEncoder)})

# The populate view
def populate(request):
    populate_database(BASE_DIR + DATA_DIR + DATA_FILE_NAME)
    return HttpResponse("Populated Successfully")

# Fetch data as JSON
def fetch_data(request):
    return JsonResponse({'compaigns': list(Compaign.objects.values())})

# Search a compaign
def search(request):
    results, message = query_database(request.GET.get('query'),request.GET.get('type'))
    return render_to_response('index.html', {"results": results, "message": message})