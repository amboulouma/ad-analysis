from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from chartit import DataPool, Chart, PivotDataPool, PivotChart

from dashboard.models import Compaign
from dashboard.algorithms import populate_database
from dashboard.constants import DATA_DIR, DATA_FILE_NAME, BASE_DIR

# Dashboard display
def index(request):
    compaigns_data = DataPool(
            series=[{'options': { 
                'source': Compaign.objects.all()},
                'terms': ['date', 'data_source', 'compaign_name', 'clicks', 'impressions']}
            ])

    compaigns_chart = Chart(
        datasource=compaigns_data,
        series_options=[{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
            'date': ['clicks', 'impressions']
        }}],
        chart_options={'title': {'text': 'Clicks and Impressions by date'},
            'xAxis': { 'title': { 'text': 'Date'}}})

    return render_to_response("index.html", {"compaigns_chart":compaigns_chart})

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
    