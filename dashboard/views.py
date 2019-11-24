from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from dashboard.models import Compaign
from dashboard.algorithms import populate_database
from dashboard.constants import DATA_DIR, DATA_FILE_NAME, BASE_DIR

# The index view
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# The populate view
def populate(request):
    populate_database(BASE_DIR + DATA_DIR + DATA_FILE_NAME)
    return HttpResponse("Populated Successfully")

# The fetch all view
def fetch_all(request):
    data = Compaign.objects.all()
    compaigns = {
        "compaigns": data
    }
    return render_to_response("results.html", compaigns)